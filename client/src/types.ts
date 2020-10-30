interface NavItems {
    title: string;
    icon: string;
    link: string;
}

interface Cell {
    x: number;
    y: number;
    w: number;
    h: number;
    i: string;
    static: boolean;
}

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

export { Coordinate, Cell, NavItems };
