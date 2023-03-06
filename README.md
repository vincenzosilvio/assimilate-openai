[![Codespaces Prebuilds](https://github.com/nogibjj/assimilate-openai/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/nogibjj/assimilate-openai/actions/workflows/codespaces/create_codespaces_prebuilds)
[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/assimilate-openai/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/assimilate-openai/actions/workflows/main.yml)

# assimilate-openai

An extensive collection of tutorials and live streams on [OpenAi](https://openai.com/)

## Day 8:  Try to build a chatGTP client from scratch


## Day 7:  More Rust

Ran into some problems with unfinished APIS.  Did find an example of chatgpt with Rust:  https://github.com/elbruno/RustOpenAIAPIs
Recap of the previous project which is in openai:

`cargo run -- complete -t "The weather in March is warmer than usual, this is because"`


## Day 6: Switching to Rust  

* install Rust via Rustup: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
Use Rust API for OpenAI (3rd party):  https://github.com/deontologician/openai-api-rust

* Create new project: `cargo new openai` and cd into it
* `make format` then `make lint` then `cargo run`

Working Example:

```bash
(.venv) @noahgift ➜ /workspaces/assimilate-openai/openai (main) $ cargo run -- complete -t "The rain in spain"
    Finished dev [unoptimized + debuginfo] target(s) in 0.14s
     Running `target/debug/openai complete -t 'The rain in spain'`
Completing: The rain in spain
Loves gets you nowhere
The rain in spain
```

`lib.rs`
```rust
/*This uses Open AI to Complete Sentences */

//accets the prompt and returns the completion
pub async fn complete_prompt(prompt: &str) -> Result<String, Box<dyn std::error::Error>> {
    let api_token = std::env::var("OPENAI_API_KEY")?;
    let client = openai_api::Client::new(&api_token);
    let prompt = String::from(prompt);
    let result = client.complete_prompt(prompt.as_str()).await?;
    Ok(result.choices[0].text.clone())
}

```


## Day 5:  Testing ChatGPT



## Day 4:  Setup prebuild for Codespaces and dive deep on Streamlit

`streamlit-apps`:  Using this as the starter.

* To run streamlit inside of Github codespaces do this:  `streamlit run streamlit/uberDemo.py --server.enableCORS=false`

## Day 3:  CI/CD and Refactor and built working streamlit app that generates code


* [how to generate code programatically](https://beta.openai.com/docs/guides/code)

## Day 2:  

* [Build Question and Answer CLI](https://github.com/nogibjj/assimilate-openai/blob/main/questionAnswerCLI.py)

## Day 1:  Exploring all of the concepts

* [YouTube](https://www.youtube.com/watch?v=lgGyDd_fQrA)
* [O'Reilly](https://learning.oreilly.com/videos/assimilate-openai/08252022VIDEOPAIML/08252022VIDEOPAIML-c1_s0/)

## References

* [twenty things with GPT-3](https://towardsdatascience.com/20-creative-things-to-try-out-with-gpt-3-2aacee3e2abf)
* [GPT-3 Use Cases](https://medium.com/eoraa-co/trending-use-cases-of-gpt-3-by-openai-56318b6a9184)
* [Top Three GPT-3](https://www.educative.io/blog/top-uses-gpt-3-deep-learning)
* [OpenAI cookbook](https://github.com/openai/openai-cookbook/tree/main/examples)
