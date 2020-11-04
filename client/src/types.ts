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
    type: string;
}

interface Loudness {
    at: string;
    value: number;
}

interface Motion {
    at: string;
    value: number;
}

interface Pressure {
    at: string;
    value: number;
}

interface Temperature {
    at: string;
    value: number;
}

interface Light {
    at: string;
    value: number;
}

interface Humidity {
    at: string;
    value: number;
}

interface Airquality {
    at: string;
    value: number;
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

export {
    Coordinate,
    Cell,
    NavItems,
    Temperature,
    Pressure,
    Motion,
    Loudness,
    Light,
    Humidity,
    Airquality,
};
