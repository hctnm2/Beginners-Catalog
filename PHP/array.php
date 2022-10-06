<?php
$mobil = array('Avanza', 'carry', 'Aplhard');
echo $mobil[0]."<br>";


$motor = array('Vario', 'Beat', 'Supra-X');
echo "Kemarin Saya Naik Motor $motor[0] ";
echo "<br>";
$makanan = array('mie goreng', 'Pizza Hut', 'Nasi goreng' );

echo $makanan[0]."<br>";
echo $makanan[1]."<br>";
echo $makanan[2]."<br>";

echo "<hr>";

$minuman = ['Teh', 'Kopi', 'Susu', 'Soda'];

echo $minuman[0]."<br>";
echo $minuman[1]."<br>";
echo $minuman[2]."<br>";
echo "<hr>";

for($i = 0; $i < count($minuman); $i++){

  echo $minuman[$i]."<br>";
}

echo "<hr>";

foreach ($minuman as $haus) {
echo $haus."<br>";
}

echo "<hr>";


$buku = [
 "penulis" => "Muh.Ridwan",
 "judul"  => "Laskar pelangi",
 "rilis" => "2021"
];

echo "Penulis= ".$buku["penulis"];
echo "<br>judul= ".$buku["judul"];
echo "<br>Tahun Rilis= ".$buku["rilis"];

echo "<hr>";
$mobil = [
"merek" => "Toyota",
"harga" => 150000000,
"ciptaan" => "japan"
];

echo "Merk Mobil = ".$mobil["merek"];
echo "<br> Harganya = ".$mobil["harga"];
echo "<br> Dari = ".$mobil["ciptaan"];







?>
