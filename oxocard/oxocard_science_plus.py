background(100,100,100)
#noStroke()

setPrecision(2)
textFont(FONT_ROBOTO_24)

const HUMIDITY_THRESHOLD = 80.0
const CO2_THRESHOLD = 800.0
const TEMP1_THRESHOLD = 24.0
const TEMP2_THRESHOLD = 27.0
const IAQ_THRESHOLD = 3.5

# 240x240 pixel display [idx starts with 0]
const HEIGHT = 240
const WIDTH = 240

const MAX_RBG_COLOR = 255


# TOOD get gradient between green, yellow and red for each
# TOOD model green/yellow/red tresholds and ranges
# TODO use common functions for drawing


def onDraw():
	while true:

		humi = getHumidity()
		co2 = getCO2()
		temperature = getTemperature()
		iaq = getIAQ()

		clear()

		drawText(10, 10,
			"_____MONITOR_____\n" +
			"Date: " + getMonth() + "/" + getDay() + "\n" +
			"Time: " + getHour() + ":" + getMinute() + ":" + getSecond()
		)

		# CO2
		if co2 > CO2_THRESHOLD:
			fill(0, 255, 0)
		else: fill(0,0,0)
		drawRectangleRounded(0, HEIGHT/2, WIDTH/2-2, HEIGHT/4-2, 10)
		drawText(10, HEIGHT/2, "CO2[ppm]\n" + co2)

		# TEMPERATURE
		if temperature > TEMP1_THRESHOLD:
			if temperature > TEMP2_THRESHOLD:
				fill(255, 0, 0)
			else:
				fill(255,215,0)
		else: fill(0,0,0)
			
		drawRectangleRounded(WIDTH/2, HEIGHT/2, WIDTH/2-2, HEIGHT/4-2, 10)
		drawText(WIDTH/2+10, HEIGHT/2, "TEMP[C]\n" + temperature)

		# HUMIDITY
		if humi > HUMIDITY_THRESHOLD:
			fill(0, 255, 0)
		else: fill(0,0,0)
		drawRectangleRounded(0, HEIGHT*3/4, WIDTH/2-2, HEIGHT/4-2, 10)
		drawText(10, HEIGHT*3/4, "HUMID[%]\n" + humi)

		# IAQ - Air Quality
		if iaq > IAQ_THRESHOLD:
			fill(0, 255, 0)
		else: fill(0,0,0)
		drawRectangleRounded(WIDTH/2, HEIGHT*3/4, WIDTH/2-2, HEIGHT/4-2, 10)
		drawText(WIDTH/2+10, HEIGHT*3/4, "IAQ\n" + iaq)		
		
		update()
		delay(5000)


	if getButton():
		if returnToMenu():
			return
