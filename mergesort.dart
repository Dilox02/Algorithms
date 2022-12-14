void main(List<String> args) {
  List<int> lista = [1, 3, 4, 6, 2, 5, 7, 8];
  List<int> lista2 = [1, 3, 2, 4, 7, 8, 5, 6];
  List<int> lista3 = [7, 2, 4, 5, 3, 1, 6, 8];

  mergesort(lista3, 0, lista.length);
}

void mergesort(List<int> lista, int i, int j) {
  if (j - i <= 1) {
    return;
  }
  int mediana = ((i + j - 1) / 2).floor();
  print("m = ${mediana}, i=${i}, j = ${j}");
  mergesort(lista, i, mediana + 1);
  mergesort(lista, mediana + 1, j);

  merge(lista, i, mediana, j);
}

void merge(List<int> lista, int i1, int m, int j2) {
  List<int> array_ausiliario = new List.filled(j2 - i1, 0, growable: true);
  int i = 0;
  int i1iniziale = i1;
  int i2 = m + 1;
  int f2 = j2 - 1;
  while (i1 <= m && i2 <= f2) {
    //print("i1:${i1}-m:${m}-i2:${i2}-i:${i}");

    if (lista[i1] < lista[i2]) {
      array_ausiliario[i] = lista[i1];
      i1++;
    } else {
      array_ausiliario[i] = lista[i2];

      i2++;
    }

    i++;
  }

  //print("${i}:${j2}:${array_ausiliario.length}");
  array_ausiliario.removeRange(i, array_ausiliario.length);

  if (i1 <= m) {
    array_ausiliario.addAll(lista.sublist(i1, m + 1));
  } else {
    array_ausiliario.addAll(lista.sublist(i2, f2 + 1));
  }
  for (int i = i1iniziale; i < j2; i++) {
    lista[i] = array_ausiliario[i - i1iniziale];
  }

  print("i did merge");
  debug(lista);
}

void debug(array_ausiliario) {
  var stringa = "";
  array_ausiliario.forEach((element) {
    stringa += "${element}  ";
  });
  print(stringa);
  stringa = "";
}
