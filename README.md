# Software Developer API

This api contains created to manage database operations separately.
User can have different permissions. 
- Read applications name
- Read application images
- Upload application image
## Installation

Clone repository
```bash
git clone https://github.com/hasanozdem1r/APPS_API.git
```
Download all required packages / libraries
```bash
pip install requirements.txt
```
Environment preparation
```bash
cd your_downloaded_folder/APPS_API/
set FLASK_APP=main
flask run
```


## API Endpoints & Params

GET all application names 
```bash
curl http://localhost/apps-api/v1/apps
```
GET images' directories with application id
```bash
curl http://localhost/apps-api/v1/images?app-id=51
```
parameter_name | parameter_type 
--- | --- | 
app-id | integer

GET application id with application name
```bash
curl http://localhost:80/apps-api/v1/apps/id?app-name=Rolly Legs 
```
parameter_name | parameter_type 
--- | --- | 
app-name | string

POST upload new images to application with application id and image path
```bash
curl http://localhost:80//apps-api/v1/images/post?app-id=51&image-path=I_am_Path.jpg
```
parameter_name | parameter_type 
--- | --- | 
app-id | integer
image-path | string

## Usage for Python & Javascript
PYTHON GET Request
```python
from requests import get
app = get('http://localhost:80/apps-api/v1/apps/id?app-name=Rolly Legs').json()
app_id: int = int(app[0][0])
print(app_id)
```
JAVASCRIPT GET Request
```javascript
const userAction = async () => {
  const response = await fetch('http://localhost/apps-api/v1/images?app-id=51');
  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson
}
```



## Project Timeline

DATE  | AVERAGE UPTIME
------------- | -------------
11/24/2021 |  2 HOURS
11/25/2021 | INTERVIEW DAY - 0 HOUR
11/26/2021  |  2 HOURS
11/27/2021  |  3 HOURS



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
[Unlicence](https://choosealicense.com/licenses/unlicence/)