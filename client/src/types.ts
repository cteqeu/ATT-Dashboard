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

interface Particle {
    pm1: number;
    pm10: number;
    pm25: number;
}

interface Particles {
    timestamp: string;
    values: Particle;
}

class Coordinate {
    alt: number;

    lat: number;

    long: number;

    pm1: number;

    pm10: number;

    pm25: number;

    constructor(alt: number, lat: number, long: number, pm1: number, pm10: number, pm25: number) {
        this.alt = alt;
        this.lat = lat;
        this.long = long;
        this.pm1 = pm1;
        this.pm10 = pm10;
        this.pm25 = pm25;
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
    Particles,
};
