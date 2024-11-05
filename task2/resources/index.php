<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <p id="heartBeat">
        <?php
            date_default_timezone_set('Europe/Tallinn');
            echo 'Heartbeat! ' . date('Y-m-d H:i:s');
        ?>
    </p>
</body>
</html>

