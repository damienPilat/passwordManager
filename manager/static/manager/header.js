//---------------------------------------------------
// JS for Side Nav animations:
// Detect user clicks w/ event listener
// Open or close side nav accordingly, reset style
//---------------------------------------------------


// Event Listener on Open btn
document.querySelector('span#openSideNav').addEventListener('click', function(){
    openNav();
});
// Event Listener on Close btn
document.querySelector('span#closeSideNav').addEventListener('click', function(){
    closeNav();
});
// Event Listener on main div
document.querySelector('#main').addEventListener('click', function(){
    closeNav();
});

// Open Side Na: show, move main div, change bg color
function openNav() {
    document.getElementById("sideNavBar").style.width = "250px";
    document.getElementById("main").style.marginRight = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}
// Close Side Nav: hide, put back div, replace bg color
function closeNav() {
    document.getElementById("sideNavBar").style.width = "0";
    document.getElementById("main").style.marginRight = "0";
    document.body.style.backgroundColor = "rgba(248, 248, 248, 0.8)";
}