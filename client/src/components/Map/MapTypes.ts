class Coordinate {
    place: string;

    lat: number;

    long: number;

    constructor(place: string, lat: number, long: number) {
        this.place = place;
        this.lat = lat;
        this.long = long;
    }
}

interface Ex {
    x: string;
 }

export { Coordinate, Ex };
