def get_bound_objects(map_asset_path, sequencer_asset_path):
    #새로운 레벨도 상관없음 (시퀀스를 사용하는 레벨이 아니어도 됨)
	world = unreal.EditorLoadingAndSavingUtils.load_map(map_asset_path)
	sequence = unreal.load_asset(sequencer_asset_path, unreal.LevelSequence)	
	range = sequence.get_playback_range()
	
	bound_objects = unreal.SequencerTools.get_bound_objects(world, sequence, sequence.get_bindings(), range)
	
	for bound_object in bound_objects:
		print 'Binding: %s' % bound_object.binding_proxy
		print 'Bound Objects: %s' % bound_object.bound_objects
		print '----\n'
        print type(bound_object.bound_objects)
        actor = bound_object.bound_objects[0]
        if type(actor) == unreal.StaticMeshActor:
            print actor
            print actor.static_mesh_component
            sm_component = sequence.add_possessable(actor.static_mesh_component)
            sm_component.set_parent(bound_object.binding_proxy)
            
            # sm = actor.static_mesh_component
            # sm = sm.static_mesh
            # print sm.get_material(0)
            # material_com = sequence.add_possessable(sm.get_material(0))
            # material_com.set_parent(sm_component)
            track = sm_component.add_track(unreal.MovieScenePrimitiveMaterialTrack)
            section = track.add_section()
            new_material = unreal.load_object(None, "/Game/ExampleContent/Effects/Materials/MI_ShapeInstance3.MI_ShapeInstance3") # whatever your material path is
            for channel in section.find_channels_by_type(unreal.MovieSceneScriptingObjectPathChannel):
                channel.set_default(new_material)
            
            


#파티클 버전
def get_bound_objects(map_asset_path, sequencer_asset_path):
    #새로운 레벨도 상관없음 (시퀀스를 사용하는 레벨이 아니어도 됨)
	world = unreal.EditorLoadingAndSavingUtils.load_map(map_asset_path)
	sequence = unreal.load_asset(sequencer_asset_path, unreal.LevelSequence)	
	range = sequence.get_playback_range()
	
	bound_objects = unreal.SequencerTools.get_bound_objects(world, sequence, sequence.get_bindings(), range)
	
	for bound_object in bound_objects:
		print 'Binding: %s' % bound_object.binding_proxy
		print 'Bound Objects: %s' % bound_object.bound_objects
		print '----\n'
        print type(bound_object.bound_objects)
        actor = bound_object.bound_objects[0]
        if type(actor) == unreal.Emitter:
            print actor
            print actor.particle_system_component
            particle_comp_bind = sequence.add_possessable(actor.particle_system_component)
            particle_comp_bind.set_parent(bound_object.binding_proxy)
            
            track = particle_comp_bind.add_track(unreal.MovieScenePrimitiveMaterialTrack)
            section = track.add_section()
            new_material = unreal.load_object(None, "/Game/ExampleContent/Effects/Materials/MI_ShapeInstance3.MI_ShapeInstance3") # whatever your material path is
            for channel in section.find_channels_by_type(unreal.MovieSceneScriptingObjectPathChannel):
                channel.set_default(new_material)


