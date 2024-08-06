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
                        echo "start build app"
                        sh 'docker build -t ved1111/docker-practise:1.0 .'
                        sh "echo $PASS | docker login -u $USER --password-stdin"
                        echo 'build successfully'
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
                        sh 'docker push ved1111/docker-practise:1.0'
                        echo 'deploy successfully'
                  }
            }
      }
}