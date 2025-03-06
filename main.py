import time
import set_completed
import quiz

def main(run_times):
    for _ in range(run_times):
        set_completed.use_existing_session()  
        time.sleep(0.5)
        quiz.submit_quiz(num_submits=10)  

if __name__ == "__main__":
    run_times = 4 
    main(run_times)
