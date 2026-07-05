---
title: "2026/07/05 本週 GitHub AI 趨勢"
date: 2026-07-05
draft: false
tags: ["GitHub趨勢", "AI週報", "AI開發工具", "生成式AI", "AI智能體"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

本週從 GitHub Trending 前 15 名中，篩選出 **15 個** AI/LLM 相關專案：

---

## 1. [usestrix/strix](https://github.com/usestrix/strix)

> [→ GitHub 連結](https://github.com/usestrix/strix)

GitHub Trending 上的 `usestrix/strix` 是一款開源 AI 滲透測試工具。它運用自主 AI 代理模擬駭客，能動態查找、驗證並自動修復應用程式漏洞，解決了傳統資安檢測耗時、誤報問題。

Strix 巧妙結合大型語言模型（LLM）能力於資安攻防，實現偵察、利用與驗證自動化。其多代理協同及 CI/CD 整合，顯著提升檢測效率與準確性。對追求 AI 驅動 DevSecOps 的團隊來說，Strix 展現了 LLM 在複雜資安任務上的巨大潛力。

---

## 2. [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

> [→ GitHub 連結](https://github.com/xbtlin/ai-berkshire)

xbtlin/ai-berkshire 是一個結合了巴菲特、芒格等四位投資大師方法論的 AI 時代價值投資研究框架。它直指當前 LLM 在投資分析中常流於表面、缺乏具體決策依據的核心痛點。此專案透過多 Agent 並行研究，模擬大師間的「思維衝突」來揭示盲點，並強制 AI 輸出「通過/不通過/灰色地帶」的明確結論。其內建的反偏見機制、利用 Python 進行的金融數據精確驗證，以及確保研究流程可複現的設計，都為 LLM 應用在複雜且高利害關係的金融決策場景樹立了嚴謹的標準。這不僅是技術社群對多 Agent 系統的實踐探索，更展示了如何將 AI 從資訊整合者轉變為深度決策輔助工具，極具參考價值。

---

## 3. [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat)

> [→ GitHub 連結](https://github.com/simplex-chat/simplex-chat)

SimpleX Chat 是一個開源通訊專案，以其「零用戶識別」的極致隱私設計，徹底顛覆了傳統通訊軟體對元數據的保護不足。它不儲存任何用戶身份或電話號碼，透過單向訊息佇列與成對、短暫的連接識別碼，確保用戶身份、通訊對象及時間等元數據在伺服器端完全不可追溯。所有數據僅儲存於客戶端，並整合了雙棘輪端到端加密、抗量子密鑰交換等先進技術，從根本上實現了無與倫比的隱私與安全。

對於AI/LLM技術社群，SimpleX Chat的價值日益顯著。隨著AI應用普及，確保用戶與模型互動時的數據隱私至關重要。SimpleX提供的安全通訊基礎，特別適合整合開源語言模型，為開發私密AI聊天機器人、安全傳輸敏感訓練數據，或進行機密AI專案討論提供了理想環境。它能有效避免對話內容和元數據被第三方窺視，為AI時代的信任通訊與數據主權提供了關鍵答案。

---

## 4. [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map)

> [→ GitHub 連結](https://github.com/Robbyant/lingbot-map)

A feed-forward 3D foundation model for reconstructing scenes from streaming data  
   
  LingBot-Map: Geometric Context Transformer for Streaming 3D Reconstruction  
  Robbyant Team  
  
  
             
  
 https://github.com/user-attachments/assets/fe39e095-af2c-4ec9-b68d-a8ba97e505ab  
  
 🗺️ Meet LingBot-Map! We've built a feed-forward 3D foundation model for streaming 3D reconstruction! 🏗️🌍  
 LingBot-Map has focused on:  
  
  Geometric Context Transformer : Architecturally unifies coordinate grounding, dense geometric cues, and long-range drift correction within a single streaming framework through anchor context, pose-reference window, and trajectory memory.  
  High-Efficiency Streaming Inference : A feed-forward architecture with paged KV cache attention, enabling stable inference at ~20 FPS on 518×378 resolution over long sequences exceeding 10,000 frames.  
  State-of-the-Art Reconstruction : Superior performance on diverse benchmarks compared to both existing streaming and iterative optimization-based approaches.  
  
  
 📑 Table of Contents  
  
 Click to expand 
   
   📰 News  
   📋 TODO  
   ⚙️ Installation  
   📦 Model Download  
   🚀 Quick Start  
   🎬 Interactive Demo ( demo.py )  
     
     Try the Example Scenes  
     Streaming with Keyframe Interval  
     Windowed Inference (for long sequences, >3000 frames)  
     Sky Masking  
     Visualization Options  
     Performance & Memory  
       
   🎥 Offline Rendering Pipeline ( demo_render/batch_demo.py )  
   📜 License  
   📖 Citation  
   ✨ Acknowledgments  
   
  
  
 📰 News  
  
  2026-06-28  — Fixed an SDPA KV cache bug.  The SDPA backend now performs better on long sequences . We still recommend the FlashInfer backend for the best performance.  
  2026-05-25  — 📊  Evaluation benchmark released . We released the evaluation scripts for KITTI and Oxford Spires — see  benchmark/  for the pipeline, and run  preprocess/oxford.py  to prepare Oxford Spires data before evaluation.  
  2026-04-29  — 📹  Long-video demo released . We released a very-long-video example (~25 000 frames, 13-minute indoor walkthrough) rendered with the offline pipeline — see  Worked Example  for the command, flag rationale, and rendered output.  
  2026-04-27  — 🚀  LingBot-Map accelerated . Pull the latest  main  and run  python demo.py --compile ...  or  python gct_profile.py --backend flashinfer --dtype bf16 --compile  to verify on your hardware.  
  2026-04-24  — Fixed a FlashInfer KV cache bug where  --keyframe_interval > 1  silently cached non-keyframes.  You should now see better pose and reconstruction quality when running with more than 320 frames .  
  
  
 📋 TODO  
  
  ✅ Release evaluation benchmark 
    
    ✅ Oxford Spires dataset  
    ✅ KITTI dataset  
    ✅ VBR dataset  
    ✅ Droid-W dataset  
    ✅ TUM-D dataset  
    ✅ 7-scenes dataset  
    ✅ ETH3D dataset  
    ✅ Tanks and Temples dataset  
    ✅ NRGBD dataset  
      
  ✅ Release demo scripts 
    
    ✅ Indoor long-video demo ( Featured indoor walkthrough )  
    ✅ Outdoor long-video demo  
    ✅ LingBot-World demo ( Worked example )  
    ✅ Aerial long-video demo  
      
  
  
 ⚙️ Installation  
 1. Create conda environment  
 conda create -n lingbot-map python=3.10 -y
conda activate lingbot-map
  
 2. Install PyTorch (CUDA 12.8)  
 pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
  
  
  PyTorch 2.8.0 is the recommended version because NVIDIA Kaolin (required by the batch rendering pipeline) has prebuilt wheels for  torch-2.8.0_cu128 . If you only need  demo.py  you may use a newer PyTorch, but the batch renderer then requires building Kaolin from source. For other CUDA versions, see  PyTorch Get Started .  
  
 3. Install lingbot-map  
 pip install -e .
  
 4. Install FlashInfer (recommended)  
 FlashInfer provides paged KV cache attention for efficient streaming inference. It is a pure-Python package that JIT-compiles CUDA kernels on first use, so a single wheel works across CUDA/PyTorch versions:  
 pip install --index-url https://pypi.org/simple flashinfer-python
  
  
  --index-url https://pypi.org/simple  is only needed if your default pip index is an internal mirror that doesn't have  flashinfer-python . (Optional) For faster first-use, you can additionally install a CUDA-specific JIT cache:  pip install flashinfer-jit-cache -f https://flashinfer.ai/whl/cu128/flashinfer-jit-cache/ . See  FlashInfer installation  for details. If FlashInfer is not installed, the model falls back to SDPA (PyTorch native attention) via  --use_sdpa .  
  
 5. Visualization dependencies (optional)  
 pip install -e ".[vis]"
  
 📦 Model Download  
  
   
    
    Model Name  
    Huggingface Repository  
    ModelScope Repository  
    Description  
    
   
   
    
    lingbot-map-long  
    robbyant/lingbot-map  
    Robbyant/lingbot-map  
    Better suited for long sequences and large scale scenes (Recommend).  
    
    
    lingbot-map  
    robbyant/lingbot-map  
    Robbyant/lingbot-map  
    Balanced checkpoint — trade off all-around performance across short and long sequences.  
    
    
    lingbot-map-stage1  
    robbyant/lingbot-map  
    Robbyant/lingbot-map  
    Stage-1 training checkpoint of lingbot-map — can be loaded into the VGGT model for bidirectional inference (c2w).  
    
   
  
  
  🚧  Coming soon:  we're training an stronger model that supports longer sequences — stay tuned.  
  
 🚀 Quick Start  
 After installation, run your first scene with one command:  
 python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/courthouse --mask_sky
  
 This launches an interactive  viser  viewer at  http://localhost:8080 . See  Interactive Demo  below for the full set of scenes and flags, or jump to  Offline Rendering Pipeline  for long-sequence batch rendering.  
 🎬 Interactive Demo ( demo.py )  
 Run  demo.py  for interactive 3D visualization via a browser-based  viser  viewer (default  http://localhost:8080 ).  
 Try the Example Scenes  
 We provide four example scenes in  example/  that you can run out of the box:  
 # courthouse scene
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/courthouse --mask_sky
  
 https://github.com/user-attachments/assets/aa10f7ab-8024-43c7-92f8-d56159ec85c8  
 # University scene
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/university --mask_sky
  
 https://github.com/user-attachments/assets/212a1744-6ff5-4ccf-9bd4-728608248b57  
 # Loop scene (loop closure trajectory)
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/loop
  
 https://github.com/user-attachments/assets/5ae0a292-b081-40c6-838c-b7c1a0538d75  
 # Oxford scene with sky masking (outdoor, large scale scene)
python demo.py --model_path /path/to/lingbot-map-long.pt \
    --image_folder example/oxford --mask_sky
  
 https://github.com/user-attachments/assets/6b8daa95-9ed4-40b2-9902-7435779b886d  
 🎯 Featured: indoor walkthrough (~25 000 frames, 13 minutes)  
 Sequence is too long for the interactive viser viewer — this clip was rendered with the  Offline Rendering Pipeline . See that section for the full command.  
 We will provide more examples in the follow-up.  
 Streaming with Keyframe Interval  
 Use  --keyframe_interval  to reduce KV cache memory by only keeping every N-th frame as a keyframe. Non-keyframe frames still produce predictions but are not stored in the cache. This is useful for long sequences which exceed 320 frames (We train with video RoPE on 320 views, so performance degrades when the KV cache stores more than 320 views. Using a keyframe strategy allows inference over longer sequences.).  
 Dataset:  Download the demo sequences from  robbyant/lingbot-map-demo  on Hugging Face.  
 Example run on the  travel  sequence from the dataset above (sky masking on, 4 camera optimization iterations, keyframe every 2 frames):  
 python demo.py \
    --image_folder /path/to/lingbot-map-demo/travel/ \
    --model_path /path/to/lingbot-map-long.pt \
    --mask_sky \
    --camera_num_iterations 4 \
    --keyframe_interval 2
  
 https://github.com/user-attachments/assets/d350b590-d036-4363-af8c-7af3918338ef  
  
  Note on inference range.  Our method does not perform state resetting by default, so the maximum inference range is bounded by the longest distance seen during training on the dataset. Beyond that distance, state resetting becomes necessary. If you observe pose collapse, switch to windowed mode ( --mode windowed ) — in most cases tuning  --keyframe_interval  alone is enough and the rest of the windowed parameters can stay at their defaults.  
  
 Windowed Inference (for long sequences, >3000 frames)  
 python demo.py --model_path /path/to/lingbot-map-long.pt \
    --video_path video.mp4 --fps 10 \
    --mode windowed --window_size 128 --overlap_keyframes 16 --keyframe_interval 2 
  
 Sky Masking  
 Sky masking uses an ONNX sky segmentation model to filter out sky points from the reconstructed point cloud, which improves visualization quality for outdoor scenes.  
 Setup:  
 # Install onnxruntime (required)
pip install onnxruntime        # CPU
# or
pip install onnxruntime-gpu    # GPU (faster for large image sets)
  
 The sky segmentation model ( skyseg.onnx ) will be automatically downloaded from  HuggingFace  on first use.  
 Usage:  
 python demo.py --model_path /path/to/checkpoint.pt \
    --image_folder /path/to/images/ --mask_sky
  
 Sky masks are cached in  <image_folder>_sky_masks/  so subsequent runs skip regeneration. You can also specify a custom cache directory with  --sky_mask_dir , or save side-by-side mask visualizations with  --sky_mask_visualization_dir :  
 python demo.py --model_path /path/to/checkpoint.pt \
    --image_folder /path/to/images/ --mask_sky \
    --sky_mask_dir /path/to/cached_masks/ \
    --sky_mask_visualization_dir /path/to/mask_viz/
  
 Visualization Options  
  
   
    
    Argument  
    Default  
    Description  
    
   
   
    
    --port  
    8080  
    Viser viewer port  
    
    
    --conf_threshold  
    1.5  
    Visibility threshold for filtering low-confidence points  
    
    
    --point_size  
    0.00001  
    Point cloud point size  
    
    
    --downsample_factor  
    10  
    Spatial downsampling for point cloud display  
    
   
  
 Performance & Memory  
 Without FlashInfer (SDPA fallback)  
 python demo.py --model_path /path/to/checkpoint.pt \
    --image_folder /path/to/images/ --use_sdpa
  
 Running on Limited GPU Memory  
 If you run into out-of-memory issues, try one (or both) of the following:  
  
  --offload_to_cpu  — offload per-frame predictions to CPU during inference (on by default; use  --no-offload_to_cpu  only if you have memory to spare).  
  --num_scale_frames 2  — reduce the number of bidirectional scale frames from the default 8 down to 2, which shrinks the activation peak of the initial scale phase.  
  
 Faster Inference  
 Lower the number of iterative refinement steps in the camera head to trade a small amount of pose accuracy for wall-clock speed:  
 python demo.py --model_path /path/to/checkpoint.pt \
    --image_folder /path/to/images/ --camera_num_iterations 1
  
 --camera_num_iterations  defaults to  4 ; setting it to  1  skips three refinement passes in the camera head (and shrinks its KV cache by 4×).  
 🎥 Offline Rendering Pipeline ( demo_render/batch_demo.py )  
 Use this pipeline when your sequence is too long for the interactive viser viewer — for example, the  indoor walkthrough featured above .  demo_render/batch_demo.py  is the all-in-one offline entry point: feed it a video or a folder of images and it will run model inference and produce a headless point-cloud flythrough MP4 in a single command. It shares the same PyTorch / FlashInfer / checkpoint stack as  demo.py .  
 For those constrained by limited VRAM or GPU usage, you may also refer to the implementation at:  https://github.com/ureeey/lingbot-map-rtx4060-8g/commit/eeee84a89cc97c1e39b736b46df4ee315275700b  
 Install (extends the main install)  
 1. Rendering Python dependencies  
 pip install -e ".[vis,render]"
  
 render  pulls in  open3d>=0.19  and  pyyaml  (the core  numpy<2  constraint comes from the base  lingbot-map  install). Sky masking in this pipeline uses  onnxruntime-gpu  for batched segmentation; install it if you don't already have the CPU  onnxruntime :  
 pip install onnxruntime-gpu
  
 2. Kaolin  — matches the PyTorch 2.8.0 + CUDA 12.8 recommended above:  
 pip install --index-url https://pypi.org/simple \
    kaolin -f https://nvidia-kaolin.s3.us-east-2.amazonaws.com/torch-2.8.0_cu128.html
  
  
  --index-url https://pypi.org/simple  bypasses any internal mirror that might otherwise serve the PyPI placeholder wheel (which raises  ImportError  on import). NVIDIA Kaolin does not publish prebuilt wheels for PyTorch 2.9.x — if you're on 2.9 for other reasons, build Kaolin from source ( pip install --no-build-isolation git+https://github.com/NVIDIAGameWorks/kaolin.git , needs local CUDA toolkit). For other torch/CUDA combinations see  NVIDIA Kaolin installation .  
  
 3. ffmpeg  
 sudo apt install ffmpeg    # or: brew install ffmpeg
  
 4. CUDA extensions  (required before first run)  
 cd demo_render/render_cuda_ext && python setup.py build_ext --inplace && cd ../..
  
 This builds  voxel_morton_ext  and  frustum_cull_ext  in place — both are imported by  rgbd_render  for GPU voxelization and frustum culling.  
 Worked Example — long indoor walkthrough (~25 000 frames, 13 minutes)  
 Dataset:  Download the example video from  robbyant/lingbot-map-demo  on Hugging Face.  
     python demo_render/batch_demo.py \
    --video_path /data/demo_videos/indoor_travel.MP4 \
    --output_folder /data/outputs/indoor_travel/ \
    --model_path /path/to/lingbot-map.pt \
    --config demo_render/config/indoor.yaml \
    --mode windowed --window_size 128 \
    --keyframe_interval 13 --overlap_keyframes 8 \
    --sky_mask_dir /data/outputs/sky_masks \
    --sky_mask_visualization_dir /data/outputs/sky_mask_viz \
    --camera_vis default --keyframes_only_points \
    --frame_tag --frame_tag_position top_right \
    --save_predictions
  
  
 Flag-by-flag rationale:  
  
   
    
    Flag  
    Why it's there  
    
   
   
    
    --mode windowed --window_size 128  
    Sliding-window inference is required once the sequence exceeds the ~320-frame RoPE training range; each window resets the KV cache.  window_size  counts KV-cache slots, not actual frames  — the first  num_scale_frames  (=8) slots hold the scale frames and the remaining  128 − 8 = 120  slots hold keyframes. With  keyframe_interval = 13 , one window therefore covers  8 + 120 × 13 = 1568  actual frames.  
    
    
    --keyframe_interval 13  
    Cache only every 13th frame as a keyframe. Non-keyframes still emit per-frame predictions but don't grow the KV cache  
    
    
    --overlap_keyframes 8  
    Adjacent windows share 8 keyframes of context, resolved internally to  max(num_scale_frames, 8 × keyframe_interval) = 8 × 13 = 104  actual frames of overlap. Recommended whenever  keyframe_interval > 1 , to keep cross-window pose alignment stable.  
    
    
    --config demo_render/config/indoor.yaml  
    Seed render/scene/camera/overlay defaults from the indoor preset (short depth, tighter follow cam). Any CLI flag the user explicitly passes still overrides the YAML value.  
    
    
    --sky_mask_dir  /  --sky_mask_visualization_dir  
    Persist sky masks and their side-by-side visualizations to disk so subsequent reruns reuse them instead of re-running ONNX segmentation. (The render pipeline only consumes them when sky masking is enabled — by the YAML preset or by  --mask_sky .)  
    
    
    --camera_vis default  
    Overlay the trajectory trail + recent-frame points on the rendered video.  
    
    
    --keyframes_only_points  
    Only unproject keyframe depth into the point cloud; non-keyframes still contribute their pose to the trajectory/frustum overlay. Keeps the cloud sparse for very long sequences.  
    
    
    --frame_tag --frame_tag_position top_right  
    Stamp a  <i> / <N> Frames  counter in the top-right corner of the MP4.  
    
    
    --save_predictions  
    Persist per-frame NPZs alongside the MP4. Useful for inspection or for re-rendering with different camera/overlay settings later.  
    
   
  
 Worked Example — outdoor drive scene  
 Dataset:  Download the example video from  robbyant/lingbot-map-demo  on Hugging Face.  
     python demo_render/batch_demo.py \
    --video_path /data/demo_videos/drive_frames.mp4 \
    --output_folder /data/outputs/drive/ \
    --model_path /path/to/lingbot-map.pt \
    --config demo_render/config/outdoor_drive.yaml \
    --mode windowed --window_size 128 \
    --max_non_keyframe_gap 100 --overlap_keyframes 8 \
    --image_stride 1 \
    --sky_mask_dir /data/outputs/sky_masks \
    --sky_mask_visualization_dir /data/outputs/sky_mask_viz \
    --camera_vis default --keyframes_only_points \
    --frame_tag --frame_tag_position top_right \
    --save_predictions
  
  
 What differs from the indoor walkthrough above:  
  
   
    
    Flag  
    Why it's there  
    
   
   
    
    --config demo_render/config/outdoor_drive.yaml  
    Seed defaults from the outdoor preset: sky masking enabled, deeper render range ( max_depth: 250 ), and a follow cam tuned for vehicle trajectories with a final birdeye reveal.  
    
    
    --image_stride 1  
    Use every video frame. Increase it to subsample long or high-FPS drive footage.  
    
    
    --max_non_keyframe_gap 100  
    Upper bound on consecutive non-keyframes before a keyframe is forced. Only active with flow-based keyframe selection ( --flow_threshold > 0 ); in the default fixed-interval mode it has no effect.  
    
   
  
 The remaining flags ( --mode windowed --window_size 128 ,  --overlap_keyframes 8 , sky-mask caching, overlays,  --save_predictions ) carry over unchanged from the indoor example — see the flag-by-flag table above.  
 Worked Example — LingBot-World scenes  
 Reconstruct videos generated by LingBot-World, our world model — the same pipeline works on generated footage out of the box.  
 Dataset:  Download the example videos ( lingbo_world_frames.mp4 ,  lingbo_world2_frames.mp4 ) from  robbyant/lingbot-map-demo  on Hugging Face.  
     python demo_render/batch_demo.py \
    --video_path /data/demo_videos/lingbo_world_frames.mp4 \
    --output_folder /data/outputs/lingbo_world/ \
    --model_path /path/to/lingbot-map.pt \
    --config demo_render/config/outdoor_drive.yaml \
    --mode windowed --window_size 128 \
    --max_non_keyframe_gap 100 --overlap_keyframes 8 \
    --image_stride 1 \
    --sky_mask_dir /data/outputs/sky_masks \
    --sky_mask_visualization_dir /data/outputs/sky_mask_viz \
    --camera_vis default --keyframes_only_points \
    --frame_tag --frame_tag_position top_right \
    --save_predictions
  
 For the second clip, run the same command with  --video_path /data/demo_videos/lingbo_world2_frames.mp4 --output_folder /data/outputs/lingbo_world2/  (and separate  --sky_mask_dir  /  --sky_mask_visualization_dir  folders if you want to keep the cached masks apart).  
 All flags are identical to the  outdoor drive scene  above — only the input video and output folder change. See the drive scene and indoor walkthrough tables for the flag-by-flag rationale.  
  
  
 Camera Path (YAML)  
 The virtual camera path is described by the  camera.segments  list in the YAML preset passed via  --config . Edit the YAML to design your own shot — no need to touch CLI flags.  
 Built-in presets live in  demo_render/config/ :  default.yaml ,  indoor.yaml ,  outdoor_drive.yaml . Copy one and edit the  camera:  block.  
 YAML structure  
 camera:
  fov: 60.0          # camera field of view in degrees
  transition: 30     # frames blended between adjacent segments
  segments:
    - mode: follow            # chase cam following the input trajectory
      frames: [0, 1500]       # rendered-frame range this segment covers (-1 = end)
      back_offset: 0.3        # how far behind the input camera (fraction of scene scale)
      up_offset: 0.08         # vertical lift above the input camera
      look_offset: 0.4        # how far ahead the lookat target points
      smooth_window: 30       # trajectory smoothing window in frames
    - mode: birdeye           # rise up for a top-down reveal of the whole scene
      frames: [1500, 1800]
      reveal_height_mult: 2.5 # birdeye height = scene scale × this factor
    - mode: follow            # drop back into chase cam
      frames: [1800, -1]
      back_offset: 0.3
      up_offset: 0.08
      look_offset: 0.4
  
 transition  controls how many frames are blended between adjacent segments;  frames: [0, -1]  means "the whole sequence".  
 Available modes  
  
   
    
    mode  
    Behavior  
    Tunable fields  
    
   
   
    
    follow  
    Chase cam tracks the input trajectory with smooth offsets. The most cinematic option for walkthroughs.  
    back_offset ,  up_offset ,  look_offset ,  smooth_window ,  scale_frames  
    
    
    birdeye  
    Top-down reveal of the whole scene. Useful for hero / overview shots.  
    reveal_height_mult  
    
    
    static  
    Fixed eye + lookat, auto-derived from the segment's start frame.  
    —  
    
    
    pivot  
    Fixed eye, lookat sweeps along the trajectory.  
    —  
    
   
  
 Single-shot YAML examples  
 Pure follow  (most common):  
 camera:
  fov: 60.0
  segments:
    - mode: follow
      frames: [0, -1]
      back_offset: 0.3
      up_offset: 0.08
      look_offset: 0.4
      smooth_window: 30
  
 Full birdeye  (good for overview / hero shots):  
 camera:
  fov: 60.0
  segments:
    - mode: birdeye
      frames: [0, -1]
      reveal_height_mult: 2.5
  
 Follow with birdeye inserts : just list multiple segments in order under  segments:  — adjacent segments are interpolated using  transition  frames.  
  
  Caveat: when  --config  loads a YAML preset, passing  any  segment-shaping CLI flag ( --camera_mode ,  --back_offset ,  --up_offset ,  --look_offset ,  --smooth_window ,  --follow_scale_frames ,  --birdeye_start ,  --birdeye_duration ,  --reveal_height_mult ) discards the YAML's  segments  and rebuilds the camera path from those flags instead. To stay fully YAML-driven, don't pass any of them on the command line.  
  
 Output files  
 For a given output name (e.g.  <scene>  or  <video_name> ):  
  
   
    
    File  
    Description  
    
   
   
    
    <name>_pointcloud.mp4  
    Rendered point-cloud flythrough  
    
    
    <name>_pointcloud_rgb.mp4  
    Original RGB frames encoded as video  
    
    
    <name>_pointcloud_config.yaml  
    Full config snapshot of this run  
    
    
    batch_results.json  
    Per-scene success / duration summary  
    
   
  
 📜 License  
 This project is released under the Apache License 2.0. See  LICENSE  file for details.  
 📖 Citation  
 @article{chen2026geometric,
  title={Geometric Context Transformer for Streaming 3D Reconstruction},
  author={Chen, Lin-Zhuo and Gao, Jian and Chen, Yihang and Cheng, Ka Leong and Sun, Yipengjing and Hu, Liangxiao and Xue, Nan and Zhu, Xing and Shen, Yujun and Yao, Yao and Xu, Yinghao},
  journal={arXiv preprint arXiv:2604.14141},
  year={2026}
}
  
 ✨ Acknowledgments  
 We thank Shangzhan Zhang, Jianyuan Wang, Yudong Jin, Christian Rupprecht, and Xun Cao for their helpful discussions and support.  
 This work builds upon several excellent open-source projects:  
  
  VGGT  
  DINOv2  
  Flashinfer

---

## 5. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

> [→ GitHub 連結](https://github.com/diegosouzapw/OmniRoute)

OmniRoute 是一個強大的開源 AI 閘道，旨在簡化 AI/LLM 開發者整合多個模型與服務的複雜性。它提供單一 API 端點，支援超過 230 個 AI 供應商，其中包含近百個提供免費額度的服務，讓開發者能將 Claude Code、Copilot 等常用工具無縫串接到 Claude、GPT、Gemini 等主流模型。其核心亮點在於獨特的 RTK + Caveman 堆疊壓縮技術，能將提示詞 token 用量減少 15% 至 95%，大幅降低成本。同時，OmniRoute 具備智慧型自動故障轉移與 17 種靈活的路由策略，確保即使單一提供者額度耗盡或服務中斷，開發工作也能持續不輟。對於希望聚合免費 AI 資源、優化 token 效益並建立高度可靠 AI 基礎設施的技術社群來說，OmniRoute 提供了兼具成本效益與穩定性的卓越解決方案。

---

## 6. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

> [→ GitHub 連結](https://github.com/DeusData/codebase-memory-mcp)

DeusData 的 codebase-memory-mcp 提供高性能程式碼智慧 MCP 伺服器，能將程式碼庫快速索引成持久性知識圖譜。它解決了 AI 代理理解大型或複雜程式碼時，傳統檔案搜尋效率低、消耗大量 token 的痛點。透過結合 tree-sitter AST 解析與 Hybrid LSP 語義解析，此工具為 158 種語言構建豐富的知識圖譜，包含函數、類別、呼叫鏈等，並支援次毫秒級結構化查詢。對於 AI/LLM 領域，它扮演智能程式碼助理的「大腦」，讓 LLM 無需進行昂貴的逐檔探索，而是直接透過圖譜工具查詢精確程式碼上下文，大幅減少 99% token 消耗，提升代理效率與準確性。它可與 Claude Code、Gemini CLI 等 11 種主流 AI 代理即插即用，單一靜態執行檔且零依賴的特性，也降低部署複雜度，讓 AI 程式碼開發更流暢。

---

## 7. [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr)

> [→ GitHub 連結](https://github.com/ogulcancelik/herdr)

Herdr 是一個專為管理 AI 編碼代理而生的終端多工器，它巧妙地解決了開發者在單一終端中協調與監控多個 AI 助手所面臨的痛點。傳統的終端工具如 tmux 雖提供會話持久性，卻無法感知代理的狀態（例如「被阻擋」、「工作中」或「已完成」），而許多 GUI 代理管理器則受限於平台，且往往只是模擬終端介面。

Herdr 的核心價值在於，它為每個 AI 代理提供一個獨立的「真實終端」視窗，並透過側邊欄即時展示代理的運行狀態。這讓開發者能一眼掌握整個代理團隊的進度，大幅提升多代理協作的效率。它支援會話持久化和 SSH 遠端連接，意味著你的代理即使在斷開連接後也能持續運行。對於 AI/LLM 領域的開發者而言，Herdr 不僅是監控工具，更是一個強大的協作平台，其 Socket API 甚至允許 AI 代理反過來驅動 Herdr，實現更深層次的自動化。這代表著將 AI 協作無縫融入終端工作流的未來方向。

---

## 8. [logto-io/logto](https://github.com/logto-io/logto)

> [→ GitHub 連結](https://github.com/logto-io/logto)

Logto 是一個開源的身份驗證與授權基礎設施，專為 SaaS 和 AI 應用設計，基於 OIDC 和 OAuth 2.1 標準。它旨在解決多租戶、企業級 SSO 和 RBAC 等複雜身份管理挑戰，協助開發者輕鬆建構安全、可擴展的應用。

Logto 在 AI/LLM 領域尤其值得關注，因其明確支援「Model Context Protocol 與基於代理（agent-based）的 AI 架構」。這表示不論是開發 LLM 應用、AI Agents，或為 AI 服務提供身份驗證與權限控制，Logto 都提供了一套專為這些新興場景優化的穩健方案。

憑藉其多租戶能力和涵蓋 30+ 框架的 SDK 支援，Logto 能幫助 AI 產品團隊快速安全地整合身份管理，讓開發者專注於 AI 核心邏輯的創新，有效提升開發效率。

---

## 9. [Starmel/OpenSuperWhisper](https://github.com/Starmel/OpenSuperWhisper)

> [→ GitHub 連結](https://github.com/Starmel/OpenSuperWhisper)

Starmel 的 OpenSuperWhisper 是一個值得 macOS 用戶關注的即時語音轉文字應用。它巧妙地將 OpenAI 的 Whisper 模型（並支援 Parakeet 引擎）帶到桌面上，解決了傳統聽寫工具在準確性、多語言支援及便利性上的痛點。這款應用不僅提供即時錄音轉寫，還具備全球快捷鍵、按住錄音模式、多麥克風選擇及多語言自動偵測等實用功能。對於 AI/LLM 社群而言，OpenSuperWhisper 展示了如何將頂尖的 ASR 技術（特別是基於 Whisper.cpp 的高效能實現）產品化，讓用戶在本地端享受高效率且注重隱私的語音輸入體驗。其對 Apple Silicon 的優化和未來的串流轉寫規劃，都彰顯了其作為 Whisper 生態系中一個實用且不斷進化的典範。對於追求語音輸入效率，或是想深入了解 Whisper 應用落地的開發者與使用者，這無疑是一個強大的工具。

---

## 10. [browser-use/video-use](https://github.com/browser-use/video-use)

> [→ GitHub 連結](https://github.com/browser-use/video-use)

「browser-use/video-use」是一款開源專案，它讓 AI 代理（如 Claude Code）能像專業剪輯師一樣處理影片。使用者只需放入原始素材，透過聊天指令，AI 就能自動剪輯冗詞贅字、進行調色、生成字幕與動畫，並精準處理音訊淡入淡出，大幅簡化傳統影片製作的繁瑣流程。

此專案在 AI/LLM 領域的亮點，在於其開創性的「文字 + 隨選視覺」處理模式。LLM 不直接處理海量影像，而是依賴 ElevenLabs Scribe 的音訊轉錄稿（含精確時間戳）與按需生成的視覺複合圖。這種高效策略避免了高昂的影像幀分析成本，使 LLM 能以極低 Token 消耗，高效理解影片、進行複雜推理與自我修正。它證明了 LLM 透過結構化抽象，可將繁瑣的影片編輯轉化為智慧自動化，為多模態 AI 應用開啟全新可能。

---

## 11. [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

> [→ GitHub 連結](https://github.com/msitarzewski/agency-agents)

「msitarzewski/agency-agents」是一個開創性的 AI 代理套件，旨在解決泛用型 AI 提示詞的局限。它提供了超過 230 個高度專業化的 AI 代理，分屬於工程、設計、行銷等 16 個不同領域。每個代理都具備鮮明的個性、聚焦於明確可衡量的成果、擁有完善的工作流程及成功指標，如同一個隨時待命的 AI 專家團隊，將複雜任務拆解成精準的 AI 職能。

---

## 12. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

> [→ GitHub 連結](https://github.com/calesthio/OpenMontage)

OpenMontage 是一個開源的智能體式（agentic）影片製作系統，旨在將你的 AI 程式碼助理轉變為一個功能齊全的影片製作工作室。它解決了當前許多 AI 影片工具僅能生成單一短片、缺乏端到端工作流程的問題，透過 12 種生產管線與 52 種工具，涵蓋從市場研究、劇本撰寫、素材生成、剪輯到最終合成的全套流程，甚至能運用真實影片素材而非僅僅是圖片動畫。這個專案在 AI/LLM 領域值得關注，在於其獨特的「智能體優先」架構，將 AI 助理作為核心協調者，透過結構化的技能文件來驅動複雜的製作流程。它強調品質把關、預算控制與詳盡的決策紀錄，展現了 LLM 在多階段、高複雜度任務編排上的卓越潛力，為專業級 AI 影片製作樹立了新標準。

---

## 13. [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)

> [→ GitHub 連結](https://github.com/JCodesMore/ai-website-cloner-template)

「JCodesMore/ai-website-cloner-template」運用 AI 編碼代理，能一鍵複製任何網站並重構為現代 Next.js 程式碼庫，有效解決舊網站遷移或原始碼遺失等問題。它在 AI/LLM 領域引人注目，因其展示了 AI 代理如何透過網站偵察、設計提取與平行重建等多階段流程，自動化複雜前端開發。這不僅是簡單的程式碼生成，更彰顯了大型語言模型在軟體工程中，實現超越傳統、深度自動化協作的巨大潛力，為 AI 輔助開發模式開闢了新視角。

---

## 14. [stablyai/orca](https://github.com/stablyai/orca)

> [→ GitHub 連結](https://github.com/stablyai/orca)

stablyai/orca 是一個為 AI 輔助開發者量身打造的強大協作環境，旨在解決如何有效管理並利用「多個」平行 AI 程式碼生成代理（agent）的痛點。它將各種流行的編碼 AI，如 Claude Code、Codex 甚至 Devin 等，整合在一個統一的介面中，讓開發者能夠同時運行不同的 AI 代理，進行程式碼生成、重構或除錯。這對於日益複雜的 AI 輔助開發流程來說，提供了一站式解決方案。

Orca 最引人注目的特點是其「平行工作區」（Parallel Worktrees）機制，允許開發者將同一個需求分派給多個 AI 代理，然後比較成果並選擇最佳方案。它深度整合了 Git、提供行動端監控、遠端 SSH 工作區，甚至能讓 AI 直接與桌面應用 UI 互動。對於在 AI/LLM 領域深耕的開發者而言，Orca 不僅提升了 AI 代理的協同效率，更將開發流程從單一模型互動推向了多代理協作的新範式，是提升「100x 開發者」生產力的關鍵工具。

---

## 15. [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

> [→ GitHub 連結](https://github.com/openai/codex-plugin-cc)

openai/codex-plugin-cc 是一個專為 Claude Code 設計的外掛，它將 OpenAI 的 Codex 強大程式碼 AI 功能無縫整合至開發者的現有工作流程中。這個專案的核心在於解決開發者在不同 AI 工具間切換的痛點，讓程式碼審查、任務委派及問題偵測等工作能更流暢地完成。

它提供多種斜線指令，例如 `/codex:review` 進行標準程式碼審查，或 `/codex:adversarial-review` 進行更深入、批判性的設計挑戰。此外，`/codex:rescue` 允許將複雜任務如錯誤調查或修復直接委派給 Codex，而 `/codex:transfer` 則能將 Claude Code 中的對話上下文轉移到 Codex 應用程式中。

在 AI/LLM 領域，這個專案值得關注的原因是它展現了大型語言模型在實際開發環境中深度協作的潛力。它不僅是將 AI 工具包裝起來，更透過如「對抗性審查」這類功能，探索 LLM 作為思維夥伴的進階應用，鼓勵更嚴謹的程式碼實踐。這種跨平台整合與功能深度，預示著未來 AI 輔助開發將走向更智慧、更一體化的使用者體驗，是 LLM 如何提升開發效率和品質的實用範例。
