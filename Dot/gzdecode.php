<?php
$dir = __DIR__;
$files = array();
//检测是否存在文件
if (is_dir($dir)) {
  //打开目录
  if ($handle = opendir($dir)) {
    //返回当前文件的条目
    while (($file = readdir($handle)) !== false) {
      //去除特殊目录
      if ($file != "." && $file != "..") {
        //判断是文件还是目录
        if (is_dir($dir . "/" . $file)) {
          continue;
        } else {
          //对指定目录处理
          if(count(explode('.', $file))>1) {
            continue;
          }
          $file_use = $dir."/".$file;
          $data = file_get_contents($file_use);
          $data = iconv('UTF-8', 'ISO-8859-1', $data);
          echo gzdecode($data).PHP_EOL;
          //echo "\r\n";
        }
      }
    }
    //关闭文件夹
    closedir($handle);
  }
}