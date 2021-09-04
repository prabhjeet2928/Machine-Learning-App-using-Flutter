import 'package:flutter/material.dart';

class MyML extends StatelessWidget {
  var details = [
    {'title': 'Linear Regression', 'navigation': 'linear'},
    {'title': 'Multi Linear Regression', 'navigation': 'multilinear'},
    {'title': 'Logistic Regression', 'navigation': 'logistic'},
    {'title': 'K-Means Clustering', 'navigation': 'kmeans'},
    {'title': 'K-Nearest Neighbors', 'navigation': 'knn'},
    {'title': 'Random Forest', 'navigation': 'random'},
    {'title': 'Decision Tree', 'navigation': 'decision'},
    {'title': 'Naive Bayes Classification', 'navigation': 'naive'},
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Column(
        children: [
          SizedBox(
            height: 50,
          ),
          Text(
            "Machine Learning App",
            style: TextStyle(
                fontSize: 30,
                fontWeight: FontWeight.bold,
                color: Colors.lightBlue),
          ),
          SizedBox(
            height: 20,
          ),
          Expanded(
            child: ListView.builder(
                itemCount: details.length,
                itemBuilder: (BuildContext content, int index) {
                  return Container(
                    height: 100,
                    child: Card(
                      color: index % 2 == 0 ? Colors.lightBlue : Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10.0),
                      ),
                      margin: EdgeInsets.all(10),
                      child: ListTile(
                        title: Center(
                          child: Text("${details[index]['title']}",
                              style: TextStyle(
                                fontSize: 25,
                                fontWeight: FontWeight.bold,
                                color: index % 2 == 0
                                    ? Colors.white
                                    : Colors.black,
                              )),
                        ),
                        onTap: () => Navigator.pushNamed(
                            context, '${details[index]['navigation']}'),
                      ),
                    ),
                  );
                }),
          ),
        ],
      ),
    );
  }
}
