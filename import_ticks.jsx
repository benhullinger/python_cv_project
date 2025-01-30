try {
    var csvFile = File.openDialog("Select the tick_positions.csv file");
    if (!csvFile) {
        alert("No file selected. Exiting.");
    } else {
        csvFile.open("r");
        var doc = app.activeDocument;
        
        var firstLine = csvFile.readln();
        var tickCount = 0;
        
        while (!csvFile.eof) {
            var line = csvFile.readln();
            if (line == "") continue;
            
            var parts = line.split(",");
            if (parts.length < 2) continue;
            
            var x = parseFloat(parts[0]);
            var y = doc.height - parseFloat(parts[1]); // Flip Y coordinate
            
            // Create cross-shaped tick
            var tick = doc.pathItems.add();
            // Vertical line
            tick.setEntirePath([
                [x, y - 5],     // Bottom
                [x, y + 5],     // Top
                [x, y],         // Center
                [x - 5, y],     // Left
                [x + 5, y]      // Right
            ]);
            tick.stroked = true;
            tick.strokeWidth = 1;
            tickCount++;
        }
        csvFile.close();
        alert("Created " + tickCount + " cross-shaped tick marks!");
    }
} catch(e) {
    alert("Error: " + e + "\nLine: " + e.line);
}