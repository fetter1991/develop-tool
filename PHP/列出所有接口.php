<?php
// 设置自动加载器（如果你使用的是Composer的autoload功能）
use App\Libs\Export\ExcelHelper;

require __DIR__ . '/../bootstrap/autoload.php';
// 定义Controllers根目录（使用绝对路径或确保相对路径正确）
$controllersRoot = realpath(__DIR__ . '/../app/Http/Controllers');

if ($controllersRoot === false || !is_dir($controllersRoot)) {
    die("Controllers directory does not exist or is not readable.\n");
}

// 定义一个递归函数来遍历目录并查找PHP文件
function findControllers($dir) {
    $controllers = [];
    try {
        $files = new RecursiveIteratorIterator(
            new RecursiveDirectoryIterator($dir, RecursiveDirectoryIterator::SKIP_DOTS),
            RecursiveIteratorIterator::LEAVES_ONLY
        );

        foreach ($files as $name => $file) {
            if ($file->isDir()) {
                continue;
            } elseif (pathinfo($file, PATHINFO_EXTENSION) === 'php') {
                $className = basename($name, '.php');
                $relativePath = substr($file->getRealPath(), strlen($dir) + 1);
                $namespaceParts = explode(DIRECTORY_SEPARATOR, dirname($relativePath));
                $namespace = 'App\\Http\\Controllers\\' . implode('\\', array_map('ucfirst', $namespaceParts));
                $controllers[] = $namespace . '\\' . $className;
            }
        }
    } catch (UnexpectedValueException $e) {
        echo "Error accessing directory $dir: " . $e->getMessage() . "\n";
    }

    return $controllers;
}

// 获取所有Controller类的完全限定名
$controllers = findControllers($controllersRoot);

foreach ($controllers as $controllerClassName) {
    try {
        // 使用反射来获取Controller类的实例（不需要真正实例化对象，只需要类信息）
        $reflectionClass = new ReflectionClass($controllerClassName);

        // 检查 $privilege 属性是否存在，并且是一个数组
        if ($reflectionClass->hasProperty('privilege') &&
            $reflectionClass->getProperty('privilege')->isPublic()) {

            // 获取 $privilege 属性的值
            $privilegeProperty = $reflectionClass->getProperty('privilege');
            $privilegeProperty->setAccessible(true); // 如果属性是protected或private，则需要这一步来访问它；但在这个例子中是public，所以这一步实际上是不必要的
            $privileges[$controllerClassName] = $privilegeProperty->getValue($reflectionClass->newInstanceWithoutConstructor()); // 由于我们只需要属性值，所以不需要真正实例化对象；但newInstanceWithoutConstructor()在PHP 8.0+中已被弃用，应使用ReflectionClass::newInstance()的替代方法（如果PHP版本允许）

        } else {
            // 如果没有找到$privilege属性，或者它不是数组，或者它不是public的，我们可以记录一个错误或给它一个默认值
            $privileges[$controllerClassName] = []; // 或者抛出一个异常，取决于你的需求
        }
    } catch (ReflectionException $e) {
    }
}

$data = [];
foreach ($privileges as $key => $item){
//    if ($key != "App\Http\Controllers\Admin\DebugController"){
//        continue;
//    }
    $keyArr = explode('\\',$key);
    $controllerEn = $keyArr[count($keyArr)-1];
    $host = "";
    if (count($keyArr) == 5){
        $host = "/api/".$keyArr[3]."/". str_replace("Controller", "", $keyArr[4])."/";
    }

    if (count($keyArr) == 6){
        $host = "/api/".$keyArr[3]."/".$keyArr[4]."/". str_replace("Controller", "", $keyArr[5])."/";
    }

    $temp = [];
    if (isset($item['actions']) && !empty($item['actions'])){
        foreach ($item['actions'] as $rowKey => $row){
            $temp['file'] = $keyArr[3];
            $temp['controllerEn'] =$controllerEn;
            $temp['controllerCh'] = "";
            $temp['isJQ'] = "actions";
            $temp['jkff'] = $rowKey;
            $temp['api'] = $host.insertHyphens($rowKey);
            $temp['apiName'] = "";
            $temp['qxx'] = $row;
            if (!empty($temp)){
                $data[] = $temp;
            }
        }
    }


    $temp1 = [];
    if (isset($item['ignore']) && !empty($item['ignore'])){
        foreach ($item['ignore'] as $rowKey1 => $row1){
            $temp1['file'] = $keyArr[3];
            $temp1['controllerEn'] =$controllerEn;
            $temp1['controllerCh'] = "";
            $temp1['isJQ'] = "ignore";
            $temp1['jkff'] = $row1;
            $temp1['api'] = $host.insertHyphens($row1);
            $temp1['apiName'] = "";
            $temp1['qxx'] = "";
            if (!empty($temp1)){
                $data[] = $temp1;
            }
        }

    }
}


function insertHyphens($string) {
    $string = str_replace("Action", "", $string);
    $length = strlen($string);
    $result = $string[0]; // 保留第一个字符
    $addHyphen = false; // 标记是否需要在大写字母前添加"-"

    for ($i = 1; $i < $length; $i++) {
        $char = $string[$i];

        if (ctype_upper($char)) {
            // 如果当前字符是大写字母
            $result .= '-';
            $result .= $char;
            $addHyphen = true; // 设置标记为true，表示后续大写字母前需要添加"-"
        } else {
            // 如果当前字符是小写字母
            $result .= $char;
            $addHyphen = false; // 重置标记为false，因为小写字母后不需要添加"-"
        }
    }
    return $result;
}

exit;
//echo json_encode($data,JSON_UNESCAPED_UNICODE);exit;
ExcelHelper::ExportCSV(['文件夹', 'Controller', '名称', '是否鉴权', '接口方法', '接口方法地址', '接口方法名称', '权限项'], $data, sprintf('鉴权-%s.csv', date('Y-m-d')));
