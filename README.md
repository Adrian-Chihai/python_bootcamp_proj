Aplicația Spotify to YouTube Playlist Converter este un instrument web simplu și eficient, dezvoltat pentru a facilita transferul playlist-urile de pe Spotify pe YouTube. 
Această aplicație extrage melodiile dintr-o listă de redare Spotify și creează automat o listă de redare YouTube corespunzătoare. 
Scopul principal al aplicației este de a permite utilizatorilor să își transfere cu ușurință colecțiile de muzică între aceste două platforme populare, fără a fi nevoie să facă acest lucru manual.
**Versiunea python necesară este 3.12.**

**Instrumente necesare**
1) clonrea repositoriului:
	- `git clone https://github.com/Adrian-Chihai/python_bootcamp_proj.git`
2) instalarea dependentelor:
	- `pip install -r requirements.txt`
3) crearea contului spotify developer
	- link: https://developer.spotify.com/
	- după crearea contului poți accesa dashboardul: https://developer.spotify.com/dashboard
	- selectăm opțiunea **"Create app"**
 	- exemplu completare
	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/b95d2242-bbdc-46ca-badb-b314d353f86c)
4) salvarea cheilor spotify
	- după crearea aplicației putem accesa settings, acolo unde vom vedea cheile de care avem nevoie
	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/d16799ef-528f-463e-bb70-e821619c0168)
	- accesând settings vom vedea **Client ID**, iar pentru a vizualiza **Client secret** apasăm **view client secret**
	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/c6ec8311-4c0f-448f-96de-ea3e40b403b5)
	- în cadrul proiectul vom crea un fișier numit **.env** acolo vom salva cheile in acest format
	`SPOTIFY_CLIENT_ID=id_key
	 SPOTIFY_CLIENT_SECRET=secret_key`
5) crearea contului
	- link google console: https://g.co/kgs/dAqYRBS
	- activarea YouTube Data V3
    	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/873eb3b1-6f5c-4310-a1d4-5cb5abf759d4)
    	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/808cf285-296a-48ef-9fc0-12ba760ab1c7)
   	- creare proiect nou
   	  	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/9cd332a8-0cdc-41b6-ba2f-456bc20f0989)
   	- activarea OAuth
   	  	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/28838ad1-45e4-415d-9086-5c1f712bfed8)
   	  	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/372520fc-ec33-4031-8dd9-c3ec88fcd36c)
		- e necesara completarea doar acestor câmpuri după care apăsăm **save and continue**
   	  	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/a655cae9-de8f-40b6-90d5-fd00d733a3a6)
   	  	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/b5c385a6-f8a7-470c-b713-22ec5b93a2c6)
		- aici selectăm de care scopes avem nevoie
   		![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/1adb8bf7-498b-4ec8-97c3-2a56f9000125)
   	  	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/4932bbb8-c5dc-47e2-b2b3-c4b6ad40616c)
   	  	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/4643f9d9-0829-4413-93f2-abe4e8c19769)
   	  	- următorul pas e test users, unde ne adăugăm email-ul nostru sau alți posibil testeri
   	  	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/e1f8c4ff-b527-4651-a447-2e9198564982)
6) obținerea credențialelor
   - după ce am finisat setarea OAuth putem obține credențialele necesare urmând pașii următori
   		![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/855b8577-fe95-4796-b247-242ad9636515)
     	![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/080bd832-1ce8-4f0d-965a-ecf3ed0d102b)
   - descărcăm fișierul json și îl vom redenum client_secret
   		![image](https://github.com/Adrian-Chihai/python_bootcamp_proj/assets/104103427/8b1ed2d4-07ff-4349-b0b8-fed39c4e42d3)
   - fișierul client_secret.json trebuie copiat in folderul spotify_youtube din proiect

După executarea acestor operații puteți rula aplicatia cu comanda 
`python app.py`




