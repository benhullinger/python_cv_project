try {
    var csvFile = File.openDialog("Select curve_path.csv");
    if (!csvFile) {
        alert("No file selected. Exiting.");
    } else {
        csvFile.open("r");
        var doc = app.activeDocument;
        
        var points = [];
        var firstLine = csvFile.readln(); // Skip header
        
        while (!csvFile.eof) {
            var line = csvFile.readln();
            if (line == "") continue;
            
            var parts = line.split(",");
            if (parts.length < 2) continue;
            
            points.push([
                parseFloat(parts[0]),
                parseFloat(parts[1])
            ]);
        }
        csvFile.close();
        
        if (points.length > 0) {
            // Create new path
            var pathItem = doc.pathItems.add();
            pathItem.filled = false;
            pathItem.stroked = true;
            pathItem.strokeColor = new RGBColor();
            pathItem.strokeColor.red = 0;
            pathItem.strokeColor.green = 0;
            pathItem.strokeColor.blue = 0;
            
            // Add points to path
            for (var i = 0; i < points.length; i++) {
                var newPoint = pathItem.pathPoints.add();
                newPoint.anchor = points[i];
                newPoint.leftDirection = points[i];
                newPoint.rightDirection = points[i];
                newPoint.pointType = PointType.CORNER;
            }
            
            alert("Path created successfully with " + points.length + " points!");
        } else {
            alert("No valid points found in CSV file.");
        }
    }
} catch(e) {
    alert("Error: " + e);
}