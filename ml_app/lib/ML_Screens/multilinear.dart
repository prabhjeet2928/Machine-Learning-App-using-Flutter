import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:getwidget/getwidget.dart';

var output = "";
var rd_spend;
var admin;
var marketing;
var state;

class MultiLinearReg extends StatefulWidget {
  @override
  _MultiLinearRegState createState() => _MultiLinearRegState();
}

class _MultiLinearRegState extends State<MultiLinearReg> {
  web() async {
    var url = Uri.http("192.168.43.210", "cgi-bin/task11/multilinear.py", {
      "rd_spend": rd_spend,
      "admin": admin,
      "marketing": marketing,
      "state": state
    });
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
                        child: Image.asset(
                            "assets/Multiple-Linear-Regression.jpg"),
                      ),
                    ),
                    Container(
                      margin: EdgeInsets.only(right: 25.0),
                      alignment: Alignment.bottomRight,
                      height: 70,
                      child: Text(
                        "Multi \nLinear Regression",
                        textDirection: TextDirection.rtl,
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
              Text("Used 50_Startups Dataset for Perdict the Profit",
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.white, fontSize: 18.0)),
              SizedBox(
                height: 20,
              ),
              Container(
                child: TextField(
                  style: TextStyle(color: Colors.white),
                  onChanged: (value) {
                    rd_spend = value;
                  },
                  autocorrect: false,
                  textAlign: TextAlign.center,
                  decoration: InputDecoration(
                    hintText: "Enter R&D Spend (in float)",
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
                    admin = value;
                  },
                  autocorrect: false,
                  textAlign: TextAlign.center,
                  decoration: InputDecoration(
                    hintText: "Enter Administration (in float)",
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
                    marketing = value;
                  },
                  autocorrect: false,
                  textAlign: TextAlign.center,
                  decoration: InputDecoration(
                    hintText: "Enter Marketing Spend (in float)",
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
                height: 58,
                width: MediaQuery.of(context).size.width,
                child: DropdownButtonHideUnderline(
                  child: GFDropdown(
                    isExpanded: true,
                    padding: EdgeInsets.all(15),
                    borderRadius: BorderRadius.circular(20),
                    border: BorderSide(color: Colors.blue, width: 2),
                    dropdownButtonColor: Colors.black,
                    dropdownColor: Colors.black,
                    style: TextStyle(color: Colors.white, fontSize: 17),
                    value: state,
                    iconEnabledColor: Colors.white,
                    hint: Center(
                      child: Text(
                        "Enter State",
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
                    onChanged: (newValue) {
                      setState(() {
                        state = newValue;
                      });
                    },
                    items: [
                      'California',
                      'Florida',
                      'New York',
                    ]
                        .map((value) => DropdownMenuItem(
                              value: value,
                              child: Center(
                                child: Text(
                                  value,
                                  style: TextStyle(color: Colors.white),
                                ),
                              ),
                            ))
                        .toList(),
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
    ;
  }
}
