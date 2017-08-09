#!/bin/bash
# isalpha.sh: Использование "case" для анализа строк.

SUCCESS=0
FAILURE=-1


isfloat ()    # Проверка - состоит ли вся строка только из цифр.
{             # Другими словами - является ли строка целым числом.
  [ $# -eq 1 ] || return $FAILURE

  case $1 in
  *[!0-9.]*|"") return $FAILURE;;
  *.*.*) return $FAILURE;;
            *) return $SUCCESS;;
  esac
}

float_check ()  # Интерфейс к isdigit ().
{
if isfloat "$@"
then
  echo "\"$*\" содержит только цифры [0 - 9 или точку]."
else
  echo "\"$*\" содержит по меньшей мере один не цифровой символ."
fi

echo

}

g=27234
h=27a34
i=27.34

float_check $g
float_check $h
float_check $i
exit 0        # Сценарий дополнен S.C.

