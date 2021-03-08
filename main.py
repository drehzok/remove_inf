from pdf2image import convert_from_path

def convert_pdf_to_png(fname):
    pages = convert_from_path(fname, 500)
    for i, page in enumerate(pages):
        page.save(fname+str(i)+".png", "PNG")


from pytesseract import Output
import pytesseract
import cv2

def blacken(image, y, x):
    color = (0,0,0)
    thickness = -1
    return cv2.rectangle(image, (x[0],y[0]), (x[1],y[1]), color, thickness)


image = cv2.imread("ex.pdf0.png")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT, lang="rus")

for i in range(0, len(results["text"])):
	# extract the bounding box coordinates of the text region from
	# the current result
	x = results["left"][i]
	y = results["top"][i]
	w = results["width"][i]
	h = results["height"][i]
	# extract the OCR text itself along with the confidence of the
	# text localization
	text = results["text"][i]
	conf = int(results["conf"][i])
    # filter out weak confidence text localizations
	if conf > 90:
		# display the confidence and text to our terminal
		print("Confidence: {}".format(conf))
		print("Text: {}".format(text))
		print("")
		# strip out non-ASCII text so we can draw the text on the image
		# using OpenCV, then draw a bounding box around the text along
		# with the text itself
		text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			1.2, (0, 0, 255), 3)
# show the output image
image = blacken(image, (1600,1900), (0,5000))
cv2.imwrite('out.png', image)
