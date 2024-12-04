Title: Using HuggingFace Argument Parser
Date: 2024-12-04 10:20
Category: posts
Tags: python
Slug: hf-argument-parser
Authors: Shubhanshu Mishra
Summary: Using Huggingface Argument Parser


When writing python scripts, I rely a lot of using command line arguments to make the script reusable across different configurations. 

To support this I have been using Huggingface Argument Parser [HfArgumentParser](https://huggingface.co/docs/transformers/en/internal/trainer_utils#transformers.HfArgumentParser) for some time. This pars

The parser is a wrapper of Python's default ArgumentParser which allows specifying the arguments via dataclasses. This allows it to return specific dataclass objects after parsing the whole command line arguments. 

Some additional features we get from the HFfArgumentParser is to read the configuration from a JSON or YAML file via its `parse_json_file` and `parse_yaml_file` functions. 

Overall, I really like the ability to write arguments via dataclasses and then using the `__post_init__` to create custom arguments which I can use in the model. 

E.g. 

```python
@dataclass
class EvalArgs:
    model_name_or_path: str = field(metadata={"help": "location of the model"})
    file_suffix: str = field(default="", metadata={"help": "file_suffix for output folder"})
    batch_size: int = field(default=64, metadata={"help": "batch size"})
    max_length: int = field(default=512, metadata={"help": "max length"})
    dataset_paths: list[str] = field(default_factory=list, metadata={"help": "datasets used for the model"})
    dataset_names: list[str] = field(default_factory=list, metadata={"help": "datasets names for each dataset"})

    def __post_init__(self):
        if not self.dataset_names:
            self.dataset_names = [f"dataset_{i}" for i in range(len(self.dataset_paths))]
        assert len(self.dataset_paths) == len(self.dataset_names), f"{len(self.dataset_paths)=} != {len(self.dataset_names)=}"
        self.datasets = dict(zip(self.dataset_names, self.dataset_paths))

parser = HfArgumentParser([EvalArgs])
eval_args, unknown_args = parser.parse_args_into_dataclasses([
    "--model_name_or_path", "./model", 
    "--dataset_paths", "d1_path", "d2_path", 
    "--dataset_names", "d1", "d2", 
    "--max_length", "52"
], return_remaining_strings=True)
print(f"{eval_args=}, {unknown_args=}")
eval_args.datasets
```

Will return the following output:

```
eval_args=EvalArgs(model_name_or_path='./model', file_suffix='', batch_size=64, max_length=52, dataset_paths=['d1_path', 'd2_path'], dataset_names=['d1', 'd2']), unknown_args=[]
{'d1': 'd1_path', 'd2': 'd2_path'}
```

This allows for easily writing training and evaluation scripts for models. 
This also allows for easily reading the script from JSON or YAML files.