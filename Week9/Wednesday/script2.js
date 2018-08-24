var prompt = require('prompt-promise');
var co = require('co');

const promise = require('bluebird')

// pg-promise initialization options:
const initOptions = {
    // Use a custom promise library, instead of the default ES6 Promise:
    promiseLib: promise, 
};

// Database connection parameters:
const config = {
    host: 'localhost',
    port: 5432,
    database: 'music',
    user: 'postgres'
};

const pgp = require('pg-promise')(initOptions);
const db = pgp(config);


function doYouEvenQuery(queryString, table){

    // Add new item to Database
    db.result(queryString)
    .then(function (results) {

        // Query the ID and display the newly added item
        db.query(`SELECT id FROM ${table} ORDER BY id DESC LIMIT 1`)
        .then(function(index){
            console.log(`Created ${table} with ID ${index[0].id}.`);
        })
        .catch(function(error){
            console.log(error);
        })

    })
    .catch(function(error){
        console.log(error);
    })

}

// createAlbum();
createTrack();

function createAlbum(){

    var albumName;
    var albumYear;
    var artistID;

    prompt('Album Name: ')
    .then(function(name){
        albumName = name;
        return prompt('Album Year: ');
    })
    .then(function(year){
        albumYear = year;
        return prompt('Artist ID: ');
    })
    .then(function(id){
        artistID = id;

        doYouEvenQuery(`INSERT INTO album VALUES ( 
            DEFAULT, '${albumName}', '${albumYear}', ${parseInt(artistID)}
        );`, 'album');

        prompt.done();
    })
    .catch(function rejected(err) {
    console.log('error:', err.stack);
    prompt.finish();
    });

}

function createArtist(){

    prompt('Artist Name: ')
    .then(function(name){

        doYouEvenQuery(`INSERT INTO artist VALUES ( 
            DEFAULT, '${name}'
        );`, 'artist');

        prompt.done();
        
    })
    .catch(function rejected(err) {
    console.log('error:', err.stack);
    prompt.finish();
    });

}

function createTrack(){

    var trackName;
    var albumID;
    var trackDuration;

    prompt('Track Name: ')
    .then(function(name){
        trackName = name;
        return prompt('Album ID? ');
    })
    .then(function(album){
        albumID = album;
        return prompt('Track Duration? ');
    })
    .then(function(duration){
        trackDuration = duration;

        doYouEvenQuery(`INSERT INTO track VALUES ( 
            DEFAULT, '${trackName}', ${parseInt(albumID)}, '${trackDuration}'
        );`, 'track');

        prompt.done();

    })
    .catch(function rejected(err) {
        console.log('error:', err.stack);
        prompt.finish();
    });

}

