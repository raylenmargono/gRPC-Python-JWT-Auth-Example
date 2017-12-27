import time
from concurrent import futures

import click
import grpc

import server
from kensho_service_client.proto import kensho_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


@click.command()
@click.option('--port', default=5000)
@click.option('--max-workers', default=16)
def run(port, max_workers, grpc_interface='[::]'):
    thread_pool = futures.ThreadPoolExecutor(max_workers=max_workers)
    grpc_server = grpc.server(thread_pool=thread_pool)
    grpc_server.add_insecure_port(grpc_interface + ':' + str(port))

    kensho_pb2_grpc.add_KenshoServicer_to_server(server.KenshoServicer(), grpc_server)

    grpc_server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
