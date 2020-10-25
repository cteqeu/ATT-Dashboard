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

type Markers = Array<Coordinate>;

export { Coordinate, Markers };
