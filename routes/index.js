var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', 
  { 
    title: 'Express',
    lastCaptured: ['img01.png', 'img02.png']
  });
});

module.exports = router;
