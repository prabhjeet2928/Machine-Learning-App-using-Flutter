import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

var output = "";
var age;
var estimated_salary;

class KNNClass extends StatefulWidget {
  @override
  _KNNClassState createState() => _KNNClassState();
}

class _KNNClassState extends State<KNNClass> {
  web() async {
    var url = Uri.http("192.168.43.210", "cgi-bin/task11/knn.py",
        {"age": age, "salary": estimated_salary});
    var response = await http.get(url);
    setState(() {
      output = response.body;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.black,
        body: SingleChildScrollView(
          child: Column(
            children: [
              Container(
                width: MediaQuery.of(context).size.width * 1.0,
                height: 300,
                decoration: BoxDecoration(
                    borderRadius:
                        BorderRadius.only(bottomLeft: Radius.circular(150.0)),
                    color: Colors.lightBlue.shade600),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Center(
                      child: Container(
                        margin: EdgeInsets.only(left: 70),
                        alignment: Alignment.bottomRight,
                        width: 270,
                        height: 180,
                        child: Image.asset("assets/knn.png"),
                      ),
                    ),
                    Container(
                      margin: EdgeInsets.only(right: 25.0),
                      alignment: Alignment.bottomRight,
                      height: 70,
                      child: Text(
                        "K-Nearest Neighbors",
                        style: TextStyle(
                            fontSize: 28.0,
                            color: Colors.white,
                            fontWeight: FontWeight.bold),
                      ),
                    )
                  ],
                ),
              ),
              SizedBox(
                height: 40,
              ),
              Text(
                  "Used Social_Network_Ads Dataset for Perdict is it Purchased or not",
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.white, fontSize: 18.0)),
              SizedBox(
                height: 20,
              ),
              Container(
                child: TextField(
                  style: TextStyle(color: Colors.white),
                  onChanged: (value) {
                    age = value;
                  },
                  autocorrect: false,
                  textAlign: TextAlign.center,
                  decoration: InputDecoration(
                    hintText: "Enter Age (in int)",
                    hintStyle: TextStyle(color: Colors.white),
                    enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(20),
                        borderSide:
                            BorderSide(width: 2, color: Colors.lightBlue)),
                    focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(20),
                        borderSide:
                            BorderSide(width: 2, color: Colors.lightBlue)),
                  ),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Container(
                child: TextField(
                  style: TextStyle(color: Colors.white),
                  onChanged: (value) {
                    estimated_salary = value;
                  },
                  autocorrect: false,
                  textAlign: TextAlign.center,
                  decoration: InputDecoration(
                    hintText: "Enter Estimated Salary (in int)",
                    hintStyle: TextStyle(color: Colors.white),
                    enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(20),
                        borderSide:
                            BorderSide(width: 2, color: Colors.lightBlue)),
                    focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(20),
                        borderSide:
                            BorderSide(width: 2, color: Colors.lightBlue)),
                  ),
                ),
              ),
              SizedBox(
                height: 40,
              ),
              Material(
                color: Colors.lightBlue.shade600,
                borderRadius: BorderRadius.circular(10),
                elevation: 10,
                child: MaterialButton(
                  textColor: Colors.white,
                  minWidth: 200,
                  height: 40,
                  child: Text("Submit", style: TextStyle(fontSize: 20.0)),
                  onPressed: web,
                ),
              ),
              SizedBox(
                height: 40,
              ),
              Text("${output}",
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.white, fontSize: 20.0)),
            ],
          ),
        ));
  }
}
