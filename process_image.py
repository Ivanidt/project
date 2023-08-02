import sys
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

def process_image(input, output, network="ssd-mobilenet-v2", threshold=0.5, overlay="box", DEFAULT=False):
    #Load the recognition network
    if DEFAULT:
        print("USING DEFAULT MODEL")
        net = detectNet(network, sys.argv, threshold)
    else:
        net = detectNet(model="models/animal/ssd-mobilenet.onnx", labels="models/animal/labels.txt",
                    input_blob="input_0", output_cvg="scores", output_bbox="boxes",
                    threshold=threshold)
    input = videoSource(input, argv=sys.argv)
    output = videoOutput(output, argv=sys.argv)

    if input is None: #timeout
        return

    img = input.Capture()

    detections = net.Detect(img, overlay=overlay)

    objects = {}

    for detection in detections:
        label = net.GetClassDesc(detection.ClassID)
        confidence = detection.Confidence
        objects[label] = confidence
    
    #render the image
    output.Render(img)

    return objects

# if __name__ == "__main__":
#     objects = process_image("data/images/people1.jpg", "data/test/people_test.jpg", DEFAULT=True)
#     print(objects)