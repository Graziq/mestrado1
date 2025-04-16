from flows.hello import hello_world

if __name__ == "__main__":
    hello_world.deploy(
        name="hello-every-30min",
        schedule="*/30 * * * *",
        tags=["demo"],
    )

