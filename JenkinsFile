pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }   
        stages{
            stage('Testing'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Build'){
                steps{
                    sh "./scripts/build-images.sh"
                }
            }
            stage('Deploy App'){
                steps{
                    sh "./scripts/run.sh"
                }
            }
        }
}