# which_is_bigger
A Assesment submission project, where the prompt is taken from the "Google AI Studio" and uses "Docker Desktop" to create a container to run the code on the localhost.

# Selecting the Prompt and Getting the code.
  1. At the begining of the project, signin to the Google AI Studio url(https://aistudio.google.com/).
  2. Select the prompt. I selected "Which is Bigger". After selecting the prompt the window takes to the prompt and genai runs and give the result.
  3. In the right side of the window, there is the option "<> Get Code", After clicking the button we have a code for the prompt which we selected. Then we can copy or download it to use.
  4. And the main thing you need to have "GEMINI_API_KEY" to enhance the usability of the genai.
  5. In the left corner we have the option to "Get API key" by clicking, we will have the key.

# Setting the Docker Desktop.
  1. Download the Docker Desktop from the official site (https://www.docker.com)
  2. After downloading the application, open it and sign in with the account.
  3. Then it has a docker walkthrough to understand how docker works. It demostrate with the example "welcome_to_docker" how to add the dockerfile and how to run the docker.
  4. After the walkthrough we known about the docker how it is working.

# Instructions how to run the docker to run the code locally.
  1. We have commands to run the docker,
       1. At first, we have to build the docker,
            cmd : docker build -t which-is-bigger .
          where build -> keyword used to build the dockerfile
                t -> tag,which is the name of the docker going to build
                and the "." is mandatory
       2. Then we have to run the docker which is built,
            cmd : docker run --name genai -d -p 5002:5000 -e GEMINI_API_KEY="YOUR_API_KEY" which-is-bigger
          where run -> keyword to run the docker built
                -d -> sets the deamon off
                -p -> sets the port to 5002:5000
                then your api key to enhance the ai in the project.
       3. Then we have the command for views images,
            cmd : docker images
            which shows the detials of the docker built, with the image id, when it is created and size, tag of the image.
       4. Then, command to see the port status,
            cmd : docker ps / docker ps -a
          it shows the status of the port, port number, container id,command , name of the docker.
       5. Then, command for removing the image,
            cmd : docker rmi <imageid>
            it removes the image by knowing the image id.
    these are 5 commands that i frequently used in the process of developing this project.

after running the 2nd command we have visit the url (http://localhost:5002) to see the webapp openned.
          





