from example_1_bfv_basics import example_bfv_basics
from example_2_encoders import example_integer_encoder, example_batch_encoder, example_ckks_encoder

if __name__ == '__main__':
    print("=================== Running example 1: BFV Basics ====================")
    example_bfv_basics()
    print("=================== Running example 2: Encoders ====================")
    example_integer_encoder()
    example_batch_encoder()
    example_ckks_encoder()
