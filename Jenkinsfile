pipeline{
      agent any
      stages{
            stage("test"){
                  steps{
                        echo "test appication success"
                  }
            }
            stage("build")
            {
                  when{
                        expression{
                              BRANCH_NAME=='master'
                        }
                  }
                  steps{
                        withCredentials([usernamePassword(credentialsId: 'Ved-DockerHub', passwordVariable: 'PASS', usernameVariable: 'USER')]){
                              echo "start build app"
                              sh 'docker build -t ved1111/django-app-practise:1.1 .'
                              sh "echo $PASS | docker login -u $USER --password-stdin"
                              sh 'docker push ved1111/django-app-practise:1.1'
                              echo 'build successfully'
                        }
                  }
            }
            stage("deploy")
            {
                  when{
                        expression{
                              BRANCH_NAME=='master'
                        }
                  }
                  steps{
                        echo 'deploy successfully'
                  }
            }
      }
}