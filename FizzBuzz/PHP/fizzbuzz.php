<?php
    for ($i = 1; $i <= 100; $i++) {
        if ($i % 3 == 0 && $i % 5 != 0) {
            echo "Fizz\n";
        } elseif ($i % 3 != 0 && $i % 5 == 0) {
            echo "Buzz\n";
        } elseif ($i % 3 == 0 && $i % 5 == 0) {
            echo "FizzBuzz\n";
        } else {
            echo "$i\n";
        }
    }
?>