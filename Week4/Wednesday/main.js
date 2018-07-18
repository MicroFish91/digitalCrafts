function buildPage() {
    // Blanks out the HTML Page Body
    document.body.innerHTML = "";

    // Builds Row 1 Blue Header
    row1();

    // Rest of Site
    var bodyContent = document.createElement('div');
    bodyContent.setAttribute("class", "container");

    // Append Rows into Container
    bodyContent.appendChild(greyRow());
    bodyContent.appendChild(watchKit());
    bodyContent.appendChild(swift());

    // Append Content into Body
    document.body.appendChild(bodyContent);

}

// Builds Row 1 Blue Header
function row1(){

    // Create tags
    let row1 = document.createElement("div");
    let col11 = document.createElement("div");
    let h1 = document.createElement("h1");
    let col12 = document.createElement("div");
    let col13 = document.createElement("div");

    // Set Classes
    row1.setAttribute("class", "row header");
    col11.setAttribute("class", "col-5");
    col12.setAttribute("class", "col-3");
    col13.setAttribute("class", "col-4");

    // Add Text
    h1.textContent = "HighOnCoding";
    col12.textContent = "Home";
    col13.textContent = "Categories";

    // Add Child Divs to Row 1
    col11.appendChild(h1);
    row1.appendChild(col11);
    row1.appendChild(col12);
    row1.appendChild(col13);

    // Add to HTML Body
    document.body.appendChild(row1);

}

// Grey Row
function greyRow(){

    // Initialize tags
    let row2 = document.createElement("div");
    let h2 = document.createElement("h2");
    let br = document.createElement("br");
    let p = document.createElement("p");

    // Add Class
    row2.setAttribute("class", "header2");
    
    // Add Text
    h2.textContent = "Curse of Current Reviews";
    p.textContent = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam, iure at! Porro temporibus animi sint? Soluta, sequi aut laudantium in quam quo quisquam iure vero voluptate nemo architecto dolores beatae."

    // Append Children
    row2.appendChild(h2);
    row2.appendChild(br);
    row2.appendChild(p);

    // Return Grey Row Object
    return row2;

}

// WatchKit Row
function watchKit(){

    // Initialize Variables
    let row3 = document.createElement("div");
    let h3 = document.createElement("h3");
    let p = document.createElement("p");
    let col310 = document.createElement("div");
    let col311 = document.createElement("div");
    let col312 = document.createElement("div");

    // Add Classes
    row3.setAttribute("class", "bodyConfig");
    col310.setAttribute("class", "row comments");
    col311.setAttribute("class", "col-3");
    col312.setAttribute("class", "col-9");

    // Add text content
    h3.textContent = "Hello Watchkit";
    p.textContent = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Architecto sint reprehenderit expedita explicabo, quae inventore tempora voluptatibus modi delectus rerum, facere sed nihil dolore vero rem quasi nulla sapiente deserunt?";
    col311.textContent = "12 comments";
    col312.textContent = "124 likes";

    // Append Children
    col310.appendChild(col311);
    col310.appendChild(col312);
    row3.appendChild(h3);
    row3.appendChild(p);
    row3.appendChild(col310);

    // return object
    return row3;

}

// Swift Row
function swift(){

    // Initialize Variables
    let row4 = document.createElement("div");
    let h3 = document.createElement("h3");
    let p = document.createElement("p");
    let col310 = document.createElement("div");
    let col311 = document.createElement("div");
    let col312 = document.createElement("div");

    // Add Classes
    row4.setAttribute("class", "bodyConfig");
    col310.setAttribute("class", "row comments");
    col311.setAttribute("class", "col-3");
    col312.setAttribute("class", "col-9");

    // Add text content
    h3.textContent = "Introduction to Swift";
    p.textContent = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Architecto sint reprehenderit expedita explicabo, quae inventore tempora voluptatibus modi delectus rerum, facere sed nihil dolore vero rem quasi nulla sapiente deserunt?";
    col311.textContent = "15 comments";
    col312.textContent = "45 likes";

    // Append Children
    col310.appendChild(col311);
    col310.appendChild(col312);
    row4.appendChild(h3);
    row4.appendChild(p);
    row4.appendChild(col310);

    // return object
    return row4;

}