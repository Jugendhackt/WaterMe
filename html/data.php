<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "waterme";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM `zeitverlauf` ORDER BY timestamp DESC LIMIT 50";
$result = $conn->query($sql);
$counter = 0;
echo '{"data":[';
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo '{"id": "'.$row["id"].'","timestamp": "'.$row["timestamp"].'","data": "'.trim($row["data"]).'"}';
        $counter++;
        if ($counter < 50) {
        	echo ",";
        }
    }
} else {
	echo "{}";
}
echo ']}';
$conn->close();
?>