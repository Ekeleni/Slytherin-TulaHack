ymaps.ready(init);

function init() {
  const fileName = 'data.json';
  fetch(fileName)
    .then(response => response.json())
    .then(data => {

      const myMap = new ymaps.Map("map", {
        center: [55.751462, 37.618790],
        zoom: 10
      }, {
        searchControlProvider: 'yandex#search'
      });

      const points = [];
      for (let i = 0; i < data.points.count; i++) {
        const point = new ymaps.Placemark(data.points.coordinates[i], {
          iconImageSize: [5, 5],
          iconImageOffset: [-15, -15]
        });
        points.push(point);
      }

      const clusterer = new ymaps.Clusterer({
        preset: 'islands#invertedVioletClusterIcons',
        groupByCoordinates: false,
        clusterDisableClickZoom: true,
        clusterHideIconOnBalloonOpen: false,
        geoObjectHideIconOnBalloonOpen: false
      });

      clusterer.add(points);
      myMap.geoObjects.add(clusterer);

      const circle = new ymaps.Circle([data.coordinates, parseInt(data.radius)], null, { draggable: true });

      myMap.geoObjects.add(circle);
      const objectsInsideCircle = clusterer.getGeoObjects().filter(obj => {
        const objCoords = obj.geometry.getCoordinates();
        const distance = ymaps.coordSystem.geo.getDistance(objCoords, circle.geometry.getCoordinates());
        return distance <= circle.geometry.getRadius();
      });
      if (objectsInsideCircle.length !== 0) {
        objectsInsideCircle.forEach(obj => {
          obj.options.set('preset', 'islands#redIcon');
        });
      }
      const indexesInsideCircle = [];
      for (let i = 0; i < objectsInsideCircle.length; i++) {
        const objectIndex = points.indexOf(objectsInsideCircle[i]);
        indexesInsideCircle.push(objectIndex);
      }
      const newData = {
        points: {
          count: indexesInsideCircle.length,
          coordinates: indexesInsideCircle.map(index => data.points.coordinates[index]),
        }
      };

      const file = new File([JSON.stringify(newData)], 'datapy.json', { type: 'application/json' });
      const url = window.URL.createObjectURL(file);
      const a = document.createElement('a');
      a.setAttribute('href', url);
      a.setAttribute('download', 'datapy.json');
      a.click();
    });
}
