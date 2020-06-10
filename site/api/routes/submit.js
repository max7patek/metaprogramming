var express = require("express");
var AWS = require("aws-sdk")
var router = express.Router();
var lambda = new AWS.Lambda();
if (!AWS.config.region) {
    AWS.config.update({
      region: 'eu-west-1'
    });
  }
router.post("/", function(req, res, next) {
    var params = {
        FunctionName: 'arn:aws:lambda:us-east-1:765821332498:function:Metaprogramming', /* required */
        ClientContext: '',
        InvocationType: "RequestResponse",
        LogType: "Tail",
        Payload: "exit(0)\n" /* Strings will be Base-64 encoded on your behalf */,
        Qualifier: 'STRING_VALUE'
    };
    lambda.invoke(params, function(err, data) {
        if (err) {
            console.log(err, err.stack); // an error occurred
            res.send("{status:'ERROR'}")
        }
        else {
            console.log(data);           // successful response
            res.send(data);
        }
    });
    res.send(databaseConnection);
});

module.exports = router;