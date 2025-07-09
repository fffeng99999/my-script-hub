## 业务流程
根据代码帮我梳理业务流程，从上传代码到处理完成显示结果，以及勾选不同的选项的分支
graph TD
    A[用户访问 Demo 页面] --> B{页面初始化};
    B --> C[重置 enhancementStore 状态];

    C --> D[显示空白预览区/提示拖拽];

    D -- 用户操作 --> E{选择/拖拽图片};

    E --> F[FileDropOverlay 发出 file-dropped 事件];
    F --> G[Demo-test5-refresh4.vue 接收文件];
    G --> H[调用 enhancementStore.uploadImageAction(file)];

    H --> I[设置 isUploading = true, processingStatus = 'uploading'];
    I --> J[调用 imageProcessingApi.uploadImage(file) 进行 API 上传];
    J -- 上传成功 --> K[更新 uploadedImageId, uploadedImageUrl, processingStatus = 'completed'];
    J -- 上传失败 --> L[更新 uploadError, processingStatus = 'failed'];
    K -- 或 L --> M[isUploading = false];

    M --> N{上传成功?};
    N -- 是 --> O[图片在 ImagePreview 中显示];
    N -- 否 --> P[在页面显示上传失败信息];

    O --> Q[用户在 ControlPanel4.vue 调整参数];
    Q --> R[用户点击 "开始处理" 按钮];
    R --> S[ControlPanel4.vue 发出 process-image 事件及参数];
    S --> T[Demo-test5-refresh4.vue 接收参数];
    T --> U[调用 enhancementStore.processImageAction(parameters)];

    U --> V[设置 isProcessing = true, processingStatus = 'processing'];
    V --> W[检查 uploadedImageId 是否存在];
    W -- 否 --> X[更新 processError, processingStatus = 'failed'];
    W -- 是 --> Y[调用 imageProcessingApi.processImage(imageId, parameters) 进行 API 处理请求];
    Y -- 请求成功 --> Z[更新 processingTaskId];
    Y -- 请求失败 --> AA[更新 processError, processingStatus = 'failed'];
    Z -- 或 AA --> BB[isProcessing = false];

    BB --> CC{处理请求成功?};
    CC -- 是 --> DD[开始轮询 fetchImageResultAction];
    CC -- 否 --> EE[在页面显示处理请求失败信息];

    DD --> FF[enhancementStore.fetchImageResultAction 被周期性调用];
    FF --> GG[设置 isLoadingResult = true];
    GG --> HH[调用 imageProcessingApi.getImageResult(taskId) 获取结果];
    HH -- 结果返回 --> II{结果状态是 'completed'?};
    II -- 是 --> JJ[更新 processedResultUrl, processingStatus = 'completed'];
    II -- 是 --> KK[停止轮询];
    II -- 否 (仍在处理) --> LL[保持 isLoadingResult = false, processingStatus = 'processing'];
    HH -- 请求失败 --> MM[更新 resultError, processingStatus = 'failed'];
    MM --> KK[停止轮询];
    JJ -- 或 LL 或 MM --> NN[isLoadingResult = false];

    JJ --> OO[处理结果在 ImagePreviewResult 中显示];
    MM --> PP[在页面显示获取结果失败信息];