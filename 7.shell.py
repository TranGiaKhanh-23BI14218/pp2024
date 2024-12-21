import subprocess
import shlex

#use normal shell to run instead of default powershell 

def execute_command(command):
    try:
        # Parse the command
        if '|' in command:
            # Handle piping
            cmds = command.split('|')
            processes = []
            for i, cmd in enumerate(cmds):
                cmd = cmd.strip()
                if i == 0:
                    # First command
                    processes.append(subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE))
                elif i == len(cmds) - 1:
                    # Last command
                    processes.append(subprocess.Popen(shlex.split(cmd), stdin=processes[-1].stdout, stdout=subprocess.PIPE))
                else:
                    # Intermediate commands
                    processes.append(subprocess.Popen(shlex.split(cmd), stdin=processes[-1].stdout, stdout=subprocess.PIPE))
            output, _ = processes[-1].communicate()
            print(output.decode())
        elif '>' in command:
            # Handle output redirection
            cmd, out_file = map(str.strip, command.split('>'))
            with open(out_file, 'w') as f:
                subprocess.run(shlex.split(cmd), stdout=f)
        elif '<' in command:
            # Handle input redirection
            cmd, in_file = map(str.strip, command.split('<'))
            with open(in_file, 'r') as f:
                subprocess.run(shlex.split(cmd), stdin=f)
        else:
            # Simple command
            result = subprocess.run(shlex.split(command), capture_output=True)
            print(result.stdout.decode())
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Simple Python Shell. Type 'exit' to quit.")
    while True:
        try:
            command = input("shell> ")
            if command.lower() == 'exit':
                break
            if command.strip():
                execute_command(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except EOFError:
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()
