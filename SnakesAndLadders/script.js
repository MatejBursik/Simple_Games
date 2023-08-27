let boardSize = 9;
let row = 10;
let end = boardSize*row;
let scale = 50;
let maxLoop = 10;

let snakesNum = 6;
let snakes = [];
let laddersNum = 6;
let ladders = [];

// generating game board
const svg = document.getElementById('svg');
svg.setAttribute('width',(row*scale)+((row-1)*(scale*0.1))+(2*scale));
svg.setAttribute('height',(boardSize*scale)+((boardSize-1)*(scale*0.1))+(2*scale));


// generating board squares
function isOdd(x) { return x & 1;};

let counter = 0;
let spacerY = ((boardSize-1)*(scale*0.1))-scale;
let spacerX = 0;
let svgInnerHTMl = svg.innerHTML;

for(let line=boardSize; line > 0; line--){
    if(isOdd(line)){
        spacerX = (row-1)*(scale*0.1);
        for(let space=row-1; space > -1; space--){
            counter++;
            svgInnerHTMl += '<rect x="' + ((space*scale)+scale+spacerX) + 
                                '" y="' + ((line*scale)+scale+spacerY) + 
                                '" id="' + counter + 
                                '" width="' + scale + 
                                '" height="' + scale + 
                                '" style="fill:white" />\n<text x="' + ((space*scale)+(scale*1.3)+spacerX) + 
                                '" y="' + ((line*scale)+(scale*1.55)+spacerY) + '" fill="red" font-size="' + (scale*0.33) + 'px">' + counter + '</text>\n';
            spacerX -= scale*0.1;
        };
        spacerX = 0;
    }else{
        for(let space=0; space < row; space++){
            counter++;
            svgInnerHTMl += '<rect x="' + ((space*scale)+scale+spacerX) + 
                                '" y="' + ((line*scale)+scale+spacerY) + 
                                '" id="' + counter + 
                                '" width="' + scale + 
                                '" height="' + scale + 
                                '" style="fill:white" />\n<text x="' + ((space*scale)+(scale*1.3)+spacerX) + 
                                '" y="' + ((line*scale)+(scale*1.55)+spacerY) + '" fill="red" font-size="' + (scale*0.33) + 'px">' + counter + '</text>\n';
            spacerX += scale*0.1;
        };
        spacerX = (row-1)*(scale*0.1);
    };
    spacerY -= scale*0.1;
};
svg.innerHTML = svgInnerHTMl;

// generating players
var tile = document.getElementById('1');
svgInnerHTMl += '\n<image href="img/white.png" x="' + (parseInt(tile.getAttribute('x'))+(Math.floor(scale/4)))
                                      + '" y="' + (parseInt(tile.getAttribute('y'))+(Math.floor(scale/1.75)))
                                      + '" height="' + (238*(scale/700))
                                      + '" width="' + (153*(scale/700)) + '" id="player1" class="move"/>';
svgInnerHTMl += '\n<image href="img/black.png" x="' + (parseInt(tile.getAttribute('x'))+(Math.floor(scale/1.75)))
                                      + '" y="' + (parseInt(tile.getAttribute('y'))+(Math.floor(scale/4)))
                                      + '" height="' + (234*(scale/700))
                                      + '" width="' + (156*(scale/700)) + '" id="player2" class="move"/>\n\n';
svg.innerHTML = svgInnerHTMl;

// generating random snakes and ladders except start and end
let filler = [0,0];
var tile2;
let possible = [];

for(let i=2; i < end; i++){possible.push(i);};

for(let i=0; i < snakesNum; i++){
    filler[0] = possible.splice(Math.floor(Math.random() * possible.length),1);
    filler[1] = possible.splice(Math.floor(Math.random() * possible.length),1);
    filler = filler.flat();
    filler.sort(function(a, b) {return a - b;}).reverse();

    tile = document.getElementById(filler[0].toString());
    tile2 = document.getElementById(filler[1].toString());
    svgInnerHTMl += '<line x1="' + (parseInt(tile.getAttribute('x'))+(Math.floor(scale/2)))
                     + '" y1="' + (parseInt(tile.getAttribute('y'))+(Math.floor(scale/2)))
                     + '" x2="' + (parseInt(tile2.getAttribute('x'))+(Math.floor(scale/2)))
                     + '" y2="' + (parseInt(tile2.getAttribute('y'))+(Math.floor(scale/2)))
                     + '" style="stroke:purple;stroke-width:' + Math.floor(scale/15) + '" />\n';
    snakes.push(JSON.parse(JSON.stringify(filler)));
};

possible = [];
for(let i=2; i < end; i++){possible.push(i);};

let idx;
for(let i=0; i < snakes.length; i++){
    idx = possible.indexOf(snakes[i][0]);
    possible.splice(idx,1);
}

for(let i=0; i < laddersNum; i++){
    filler[0] = possible.splice(Math.floor(Math.random() * possible.length),1);
    filler[1] = possible.splice(Math.floor(Math.random() * possible.length),1);
    filler = filler.flat();
    filler.sort(function(a, b) {return a - b;});

    tile = document.getElementById(filler[0].toString());
    tile2 = document.getElementById(filler[1].toString());
    svgInnerHTMl += '<line x1="' + (parseInt(tile.getAttribute('x'))+(Math.floor(scale/2)))
                     + '" y1="' + (parseInt(tile.getAttribute('y'))+(Math.floor(scale/2)))
                     + '" x2="' + (parseInt(tile2.getAttribute('x'))+(Math.floor(scale/2)))
                     + '" y2="' + (parseInt(tile2.getAttribute('y'))+(Math.floor(scale/2)))
                     + '" style="stroke:green;stroke-width:' + Math.floor(scale/15) + '" />\n';
    ladders.push(JSON.parse(JSON.stringify(filler)));
};

svg.innerHTML = svgInnerHTMl;

console.log(snakes); // debug
console.log(ladders); // debug

// click to select active player
const dice = document.getElementById('dice');
const boxP1 = document.getElementById('boxP1');
const boxP2 = document.getElementById('boxP2');
const boxDice = document.getElementById('boxDice');

boxP1.addEventListener('click', function (e) {
    dice.setAttribute('player',"p1")
    console.log("p1"); // debug
});

boxP2.addEventListener('click', function (e) {
    dice.setAttribute('player',"p2")
    console.log("p2"); // debug
});

// winner popup
const popup = document.getElementById('popup-bc');

popup.addEventListener('click', function (e) {
    popup.style.display = "none";
});

// dice roll (added to the selected player)
const p1 = document.getElementById('p1');
const p2 = document.getElementById('p2');
const player1 = document.getElementById('player1');
const player2 = document.getElementById('player2');
const winner = document.getElementById('winner');
const moves = document.getElementById('moves');
let roll = 0;
let pos = 0;
let update;
let looping;

boxDice.addEventListener('click', function (e) {
    roll = Math.floor(Math.random() * 6) + 1;

    switch(dice.getAttribute('player')) {
        case "p1":
            pos = parseInt(p1.getAttribute('pos'),10);
            pos += roll;
            if(pos>end){pos=end-(pos-end)};
            console.log("pos " + pos); // debug
            p1.setAttribute('pos',pos.toString());
            tile = document.getElementById(pos.toString());
            player1.setAttribute('x',parseInt(tile.getAttribute('x'))+(Math.floor(scale/4)));
            player1.setAttribute('y',parseInt(tile.getAttribute('y'))+(Math.floor(scale/1.75)));
            p1.setAttribute('moves',parseInt(p1.getAttribute('moves'))+1);
            break;

        case "p2":
            pos = parseInt(p2.getAttribute('pos'),10);
            pos += roll;
            if(pos>end){pos=end-(pos-end)};
            console.log("pos " + pos); // debug
            p2.setAttribute('pos',pos.toString());
            tile = document.getElementById(pos.toString());
            player2.setAttribute('x',parseInt(tile.getAttribute('x'))+(Math.floor(scale/1.75)));
            player2.setAttribute('y',parseInt(tile.getAttribute('y'))+(Math.floor(scale/4)));
            p2.setAttribute('moves',parseInt(p2.getAttribute('moves'))+1);
            break;

        default:
            console.log("Error")};
    
    // Snake and Ladder activation
    update = true;
    looping = 0
    while(update && looping <= maxLoop){
        update = false;
        looping++;
        for(let i=0; i < laddersNum; i++){
            if(parseInt(p1.getAttribute('pos'),10) === ladders[i][0]){
                p1.setAttribute('pos',ladders[i][1]);
                tile = document.getElementById(ladders[i][1].toString());
                player1.setAttribute('x',parseInt(tile.getAttribute('x'))+(Math.floor(scale/4)));
                player1.setAttribute('y',parseInt(tile.getAttribute('y'))+(Math.floor(scale/1.75)));
                update = true;
                console.log("ladder"); // debug
            }
            else if(parseInt(p2.getAttribute('pos'),10) === ladders[i][0]){
                p2.setAttribute('pos',ladders[i][1]);
                tile = document.getElementById(ladders[i][1].toString());
                player2.setAttribute('x',parseInt(tile.getAttribute('x'))+(Math.floor(scale/1.75)));
                player2.setAttribute('y',parseInt(tile.getAttribute('y'))+(Math.floor(scale/4)));
                update = true;
                console.log("ladder"); // debug
            };
        };

        for(let i=0; i < snakes.length; i++){
            if(parseInt(p1.getAttribute('pos'),10) === snakes[i][0]){
                p1.setAttribute('pos',snakes[i][1]);
                tile = document.getElementById(snakes[i][1].toString());
                player1.setAttribute('x',parseInt(tile.getAttribute('x'))+(Math.floor(scale/4)));
                player1.setAttribute('y',parseInt(tile.getAttribute('y'))+(Math.floor(scale/1.75)));
                update = true;
                console.log("snake"); // debug
            }
            else if(parseInt(p2.getAttribute('pos'),10) === snakes[i][0]){
                p2.setAttribute('pos',snakes[i][1]);
                tile = document.getElementById(snakes[i][1].toString());
                player2.setAttribute('x',parseInt(tile.getAttribute('x'))+(Math.floor(scale/1.75)));
                player2.setAttribute('y',parseInt(tile.getAttribute('y'))+(Math.floor(scale/4)));
                update = true;
                console.log("snake"); // debug
            };
        };
    };

    // victory checker
    if((parseInt(p1.getAttribute('pos'),10) === end) && (p1.getAttribute('winner') === "false")){
        winner.innerText = "1";
        moves.innerText = p1.getAttribute('moves');
        popup.style.display = "block";
        p1.setAttribute('winner',"true");
    } else if((parseInt(p2.getAttribute('pos'),10) === end) && (p2.getAttribute('winner') === "false")){
        winner.innerText = "2";
        moves.innerText = p2.getAttribute('moves');
        popup.style.display = "block";
        p2.setAttribute('winner',"true");
    };
    
    console.log("roll " + roll); // debug
});
