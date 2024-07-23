const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const waterButton = document.getElementById('waterButton');
const restartButton = document.getElementById('restartButton');
const endButton = document.getElementById('endButton');
const sewerButton = document.getElementById('sewerButton');
const greenButton = document.getElementById('greenButton');
const permButton = document.getElementById('permButton');

let water = false;
let addCondition = true;
let stormwaterSewer = false;
let permeable = false;
let greenRoofs = false;

let city = new Image();
city.src = 'city_fitted.png';
city.onload = () => ctx.drawImage(city, 0, 0);

function drawButton(element, color, text) {
    element.style.backgroundColor = color;
    element.textContent = text;
}

function resetGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(city, 0, 0);
    addCondition = true;
    stormwaterSewer = false;
    permeable = false;
    greenRoofs = false;
    water = false;
    drawButton(waterButton, 'silver', 'Add Water');
    drawButton(sewerButton, 'silver', '1');
    drawButton(greenButton, 'silver', '2');
    drawButton(permButton, 'silver', '3');
    city.src = 'city_fitted.png';
    city.onload = () => ctx.drawImage(city, 0, 0);
}

waterButton.addEventListener('click', () => {
    water = !water;
    if (water) {
        if (!stormwaterSewer && !permeable && !greenRoofs) {
            city.src = 'flooded.jpg';
        } else if (stormwaterSewer && !permeable && !greenRoofs) {
            city.src = 'stormwater_drain.jpg';
        } else if (!stormwaterSewer && permeable && !greenRoofs) {
            city.src = 'permeable_walkways.jpg';
        } else if (!stormwaterSewer && !permeable && greenRoofs) {
            city.src = 'green_roofed_water.jpg';
        }
    } else {
        city.src = 'city_fitted.png';
    }
    // city.style.height = '800px';
    city.width = '1000px';
    city.onload = () => ctx.drawImage(city, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawButton(waterButton, 'silver', water ? 'Dry' : 'Add Water');
});

restartButton.addEventListener('click', resetGame);

endButton.addEventListener('click', () => {
    window.close();
});

sewerButton.addEventListener('click', () => {
    if (addCondition) {
        stormwaterSewer = true;
        addCondition = false;
        drawButton(sewerButton, 'white', '1');
    }
});

greenButton.addEventListener('click', () => {
    if (addCondition) {
        greenRoofs = true;
        addCondition = false;
        drawButton(greenButton, 'white', '2');
    }
});

permButton.addEventListener('click', () => {
    if (addCondition) {
        permeable = true;
        addCondition = false;
        drawButton(permButton, 'white', '3');
    }
});