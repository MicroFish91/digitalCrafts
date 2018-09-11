let db = require('./models'); //reads index.js

// db.user.create({firstName: 'Sam', lastName: 'Segal', email: 'me2@me.com'})
// .then(function(results){
//     console.log(results);
// })
// .catch(function(error){
//     console.log(error);
// })

// db.user.findAll()
// .then(function(results){
//     results.forEach(function(record){
//         console.log(record.id + " " + record.firstName);
//     })
// })

// db.user.findById(1)
// .then(function(result){
//     console.log(result.firstName);
// })

// db.user.findAll({where: {id: 0}})
// .then(function(result){

//     console.log(result);

//     result.forEach(function(index){
//         console.log(index.id);
//     })
// });

// db.user.destroy({where: {id: 1}})
// .then(function(results){
//     if (results === 1){
//         console.log('deleted successfully');
//     }
// });

db.sequelize.query('SELECT * FROM users' {tye: sequelize.QueryTypes.SELECT})
.then(function(results){
    console.log(results);
})