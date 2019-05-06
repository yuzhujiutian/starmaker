<?php
echo __DIR__;
echo '<br/>';


$data = file_get_contents("C:/Package/starmaker-qa/Dot/2");
$data = iconv('UTF-8', 'ISO-8859-1', $data);
echo gzdecode($data);
