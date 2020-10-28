#ifndef APP_H
#define APP_H

#include <arduino.h>
#include <stdbool.h>
#include <stdint.h>
#include <app_defs.h>
#include <ATT_GPS.h>
#include <ATT_NBIOT.h>
#include <Wire.h>
#include <Adafruit_Sensor.h> #include <Adafruit_BME280.h>
#include <DS3231.h>

namespace pxl
{
    using struct DateTime
    {
        uint8_t year;
        uint8_t month;
        uint8_t day;
        uint8_t dow;
        uint8_t hours;
        uint8_t Minutes;
        uint8_t seconds;
    } dateTime_t;

    class App
    {
        public:
            /* --------- Constructor / Destructor ---------- */
            App(void);
            ~App(void);

            uploadData(void);
            printDebugData(void);

            /* ----------  Getters ---------- */
            getDateTime(void);

            /* ----------  Setters ---------- */
            setDateTime(dateTime_t dateTime);

        private:
            /* ---------- Class variables  ----------  */
            static ATT_NBIOT       device;
            static ATT_GPS         gps(APP_DEFS_GPS_RX_PIN, APP_DEFS_GPS_TX_PIN);
            static DS3231          rtc;
            static Adafruit_BME280 bme;
            static dateTime_t      dateTime;

            static uint32_t curTime = 0u;
            static uint32_t ctime   = 0u;
            static bool     century = false;
    };
};

#endif/*APP_H*/
