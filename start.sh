if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/COLD-ONEZ/Cx-Rqst-Filter.git /Cx-Rqst-Filter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Cx-Rqst-Filter
fi
cd /Cx-Rqst-Filter
pip3 install -U -r requirements.txt
echo "Starting DQ-The-File-Donor...."
python3 bot.py
