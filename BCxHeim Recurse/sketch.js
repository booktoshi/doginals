//credit to @MartinSeeger2 on X /content/416d1b1439031393a968ec2394498aaf256c3a4ca5da2dcc656e5a726806f809i0

let img;
let metadata = {};
let traitIndex = [];
let baseImageResolution = { width: 1413, height: 1413 }; // Default values

function preload() {
    // Use a base64 image string here
    let base64Image = 'data:image/png;base64,<Your Stiched Image in bace64>';
    console.log("Loading image from base64 string");
    img = loadImage(base64Image, () => extractMetadata(base64Image));
}

function extractMetadata(base64Image) {
    console.log("Extracting metadata from base64 string");
    let data = base64Image.split(',')[1]; // Remove the 'data:image/png;base64,' part
    let binaryData = atob(data); // Decode base64 string
    let buffer = new ArrayBuffer(binaryData.length);
    let uint8Array = new Uint8Array(buffer);
    for (let i = 0; i < binaryData.length; i++) {
        uint8Array[i] = binaryData.charCodeAt(i);
    }

    let textData = new TextDecoder("utf-8").decode(uint8Array);

    // Find the start of the JSON metadata
    let metadataStart = textData.indexOf('{"base_image_resolution"');
    if (metadataStart !== -1) {
        // Use a balanced bracket method to find the end of the JSON object
        let depth = 0;
        let metadataEnd = metadataStart;
        while (metadataEnd < textData.length) {
            if (textData[metadataEnd] === '{') {
                depth++;
            } else if (textData[metadataEnd] === '}') {
                depth--;
                if (depth === 0) {
                    metadataEnd++;
                    break;
                }
            }
            metadataEnd++;
        }
        let metadataString = textData.substring(metadataStart, metadataEnd);

        console.log("Raw metadata string:", metadataString);
        try {
            metadata = JSON.parse(metadataString);
            console.log("Parsed metadata:", metadata);
            baseImageResolution = metadata.base_image_resolution;

            // Get the trait index from the HTML
            let traitIndexDiv = document.getElementById('traitindex').textContent.trim();
            traitIndex = traitIndexDiv.match(/.{1,2}/g); // Split into groups of 2 characters
            console.log("Trait index parsed:", traitIndex);
        } catch (e) {
            console.error("Error parsing metadata JSON:", e);
        }
    } else {
        console.error("Metadata not found in the image.");
    }
}

function setup() {
    createCanvas(windowWidth, windowHeight);
    console.log("Canvas created");
}

function draw() {
    background(255);
    if (img && traitIndex.length > 0 && Object.keys(metadata).length > 0) {
        console.log("Drawing image portions");
        let traitTypes = Object.keys(metadata.attributes);
        for (let i = 0; i < traitIndex.length; i++) {
            let traitCode = traitIndex[i];
            if (i < traitTypes.length) {
                let traitType = traitTypes[i];
                console.log(`Processing trait code: ${traitCode} for trait type: ${traitType}`);
                let trait = getTraitByCode(traitCode, traitType);
                if (trait) {
                    console.log(`Drawing trait: ${trait.value} at coordinates:`, trait.coordinates);
                    let portion = img.get(trait.coordinates.x, trait.coordinates.y, baseImageResolution.width, baseImageResolution.height);

                    // Calculate the dimensions to maintain the aspect ratio
                    let aspectRatio = baseImageResolution.width / baseImageResolution.height;
                    let displayWidth, displayHeight;

                    if (windowWidth / windowHeight > aspectRatio) {
                        displayHeight = windowHeight;
                        displayWidth = displayHeight * aspectRatio;
                    } else {
                        displayWidth = windowWidth;
                        displayHeight = displayWidth / aspectRatio;
                    }

                    // Center the image
                    let xOffset = (windowWidth - displayWidth) / 2;
                    let yOffset = ((windowHeight - displayHeight) / 2) - (0.00 * windowHeight); // Move up by 5%

                    image(portion, xOffset, yOffset, displayWidth, displayHeight);
                } else {
                    console.warn(`Trait not found for code: ${traitCode} in trait type: ${traitType}`);
                }
            } else {
                console.warn(`Trait index ${i} exceeds available trait types.`);
            }
        }
        noLoop(); // Stop draw loop after processing all trait codes
    }
}

function getTraitByCode(code, traitType) {
    if (code.length !== 2) {
        console.error(`Invalid trait code length: ${code}`);
        return null;
    }

    let index = parseInt(code, 10) - 1;

    let traits = metadata.attributes[traitType];

    console.log(`Index: ${index} for trait type: ${traitType}`);
    console.log(`Available traits for ${traitType}:`, traits);

    if (index >= 0 && index < traits.length) {
        return traits[index];
    } else {
        console.error(`Index out of range: ${index} for trait type: ${traitType}`);
    }
    return null;
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
    console.log("Canvas resized");
    redraw(); // Redraw on window resize
}
