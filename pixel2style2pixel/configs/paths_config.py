dataset_paths = {
	'celeba_train': '',
	'celeba_test': '',
	'celeba_train_sketch': '',
	'celeba_test_sketch': '',
	'celeba_train_segmentation': '',
	'celeba_test_segmentation': '',
	'ffhq': '',
    'soap_train':'/content/drive/MyDrive/soap_size1024_8k_train_test/soap_train_test8k/train_soap', ## Please change the path to the dataset
    'soap_test':'/content/drive/MyDrive/soap_size1024_8k_train_test/soap_train_test8k/test_soap'    ## Please change the path to the dataset
}

model_paths = {
	'stylegan_ffhq': 'pretrained_models/stylegan2-ffhq-config-f.pt',
    'stylegan2_soap_ada':'path/to/pretrain_stylegan2-ada.pt',  ## Please change the path to the model checkpoint. You will need to convert the .pkl to .pt first.
	'ir_se50': '/content/drive/MyDrive/pixel2style2pixel/pretrained_models/model_ir_se50.pth',
	'circular_face': 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': 'pretrained_models/mtcnn/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat',
  'moco': '/content/drive/MyDrive/pixel2style2pixel/pretrained_models/moco_v2_800ep_pretrain.pt'
	#'moco': 'pretrained_models/moco_v2_800ep_pretrain.pth.tar'
}
