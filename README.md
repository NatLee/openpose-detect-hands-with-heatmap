<div align="center" style="text-align: center">

# **Detect Hands By Using Open Pose with Heat Map**

<p style="text-align: center">
  <img align="center" src="./doc/original-frame.png" alt="frame" width="30%" height="100%">
  <img align="center" src="./doc/heatmap.png" alt="heatmap" width="30%" height="100%">
  <img align="center" src="./doc/heatmap-motion.gif" alt="motion" width="30%" height="100%">
</p>

</div>

> Source from [요룰레히 9_21- HEYYEYAAEYAAAEYAEYAA (What's Up)](https://www.youtube.com/watch?v=u6w9HYmQMgQ)

## Model

You can get the pre-trained model from Hugging Face.

Download it into `./model`.

https://huggingface.co/NatLee/openpose-keras-model

```bash
git clone --depth=1 git@hf.co:NatLee/openpose-keras-model ./model/
```

```
model
└── weights.h5
```

## Usage

> Tested on x86/64 CPU, Intel 12th-i5 with 16 GB RAM.

1. Prepare the model from [#Model](#model).

2. Prepare your video in `./data` named `test.mp4`.

3. Just run docker command with the following:

    ```bash
    docker-compose build && docker-compose up
    ```

## Contributor

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/NatLee"><img src="https://avatars.githubusercontent.com/u/10178964?v=3?s=100" width="100px;" alt="Nat Lee"/><br /><sub><b>Nat Lee</b></sub></a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## LICENSE

[AFLv3](LICENSE)
